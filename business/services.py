"""
Business Logic Services
Handles business operations and workflows
"""

from datetime import date, datetime, timedelta
from typing import List, Dict, Any, Optional
from decimal import Decimal

from database.repositories import (
    TransaksiRepository,
    TransaksiDetailRepository,
    DealerRepository,
    StokMotorRepository,
    LeasingRepository,
    DokumenRepository,
    CatatanRepository,
    PembayaranRepository,
)
from database.models import Transaksi, TransaksiDetail, Catatan, Pembayaran
from business.validators import (
    TransaksiValidator,
    TransaksiDetailValidator,
    StokMotorValidator,
    PriceValidator,
)
from business.exceptions import (
    RecordNotFound,
    ValidationException,
    InventoryException,
    FinancialException,
)


class TransaksiService:
    """Service for transaction management"""

    def __init__(self):
        self.repo = TransaksiRepository()
        self.detail_repo = TransaksiDetailRepository()
        self.dealer_repo = DealerRepository()
        self.motor_repo = StokMotorRepository()
        self.dokumen_repo = DokumenRepository()
        self.catatan_repo = CatatanRepository()
        self.pembayaran_repo = PembayaranRepository()
        self.validator = TransaksiValidator()
        self.detail_validator = TransaksiDetailValidator()

    # =====================================================================
    # CREATE TRANSACTION
    # =====================================================================

    def create_transaksi(self, data: Dict[str, Any]) -> Transaksi:
        """
        Create new transaction with validation and related records.

        Args:
            data: Transaction data dictionary

        Returns:
            Created Transaksi instance
        """
        # Validate
        self.validator.validate_create(data, self.repo)

        # Check motor exists and is available
        motor_id = data.get("motor_id")
        motor = self.motor_repo.get_by_id(motor_id)
        if not motor:
            raise RecordNotFound("Motor", motor_id)

        if motor.status != "R":
            raise InventoryException(f"Motor {motor.no_mesin} tidak siap dijual")

        # Get OTR from motor BEFORE any database operations that might close session
        otr = float(motor.type_motor.otr or 0) if motor and motor.type_motor else 0

        # Check dealer exists
        dealer_id = data.get("dealer_id")
        dealer = self.dealer_repo.get_by_id(dealer_id)
        if not dealer:
            raise RecordNotFound("Dealer", dealer_id)

        # Create transaction (remove financial data from transaction data first)
        transaksi_create_data = {k: v for k, v in data.items()
                                 if k not in ['harga_dasar', 'sistem_pembayaran', 'ketentuan_dp', 'dp', 'tgl_bayar_dp',
                                            'ket_dp', 'subsidi', 'diskon', 'diskon_tambahan', 'diskon_ahm', 'diskon_dealer', 'diskon_leasing',
                                            'insentif', 'hutang_sales', 'tgl_hutang_dibayar', 'leasing_id']}
        transaksi = self.repo.create(transaksi_create_data)

        # Create detail record with financial data
        tgl_bayar_dp = data.get("tgl_bayar_dp")
        if tgl_bayar_dp and isinstance(tgl_bayar_dp, str) and tgl_bayar_dp.strip():
            tgl_bayar_dp = datetime.strptime(tgl_bayar_dp, "%Y-%m-%d").date()
        else:
            tgl_bayar_dp = None

        # tgl_hutang_dibayar harus selalu None saat membuat transaksi baru
        # Hanya bisa diupdate melalui payment settlement API
        tgl_hutang_dibayar = None

        # Calculate hutang before creating detail
        sistem_pembayaran = data.get("sistem_pembayaran", "Cash")
        ketentuan_dp = float(data.get("ketentuan_dp", 0) or 0)
        dp = float(data.get("dp", 0) or 0)
        subsidi = float(data.get("subsidi", 0) or 0)
        diskon_ahm = float(data.get("diskon_ahm", 0) or 0)
        diskon_dealer = float(data.get("diskon_dealer", 0) or 0)
        diskon_leasing = float(data.get("diskon_leasing", 0) or 0)

        # Import calculate_debts from app
        import sys
        sys.path.insert(0, '/'.join(__file__.split('/')[:-2]))
        from app import calculate_debts

        hutang = calculate_debts(sistem_pembayaran, otr, ketentuan_dp, dp, subsidi, diskon_ahm, diskon_dealer, diskon_leasing)

        detail_data = {
            "transaksi_id": transaksi.id,
            "harga_dasar": data.get("harga_dasar", 0),
            "otr": otr,
            "sistem_pembayaran": sistem_pembayaran,
            "ketentuan_dp": ketentuan_dp,
            "dp": dp,
            "tgl_bayar_dp": tgl_bayar_dp,
            "ket_dp": data.get("ket_dp"),
            "subsidi": subsidi,
            "diskon_ahm": diskon_ahm,
            "diskon_dealer": diskon_dealer,
            "diskon_leasing": diskon_leasing,
            "insentif": data.get("insentif", 0),
            "hutang_sales": hutang['hutang_sales'],
            "hutang_leasing": hutang['hutang_leasing'],
            "tgl_hutang_dibayar": tgl_hutang_dibayar,
            "leasing_id": int(data.get("leasing_id")) if data.get("leasing_id") else None,
        }
        self.detail_repo.create(detail_data)

        # Update motor status to sold
        self.motor_repo.update(motor_id, {"status": "S", "tgl_status": datetime.utcnow()})

        # Add initial catatan
        self.catatan_repo.create({
            "transaksi_id": transaksi.id,
            "konten": "Transaksi baru dibuat",
            "tipe_catatan": "HISTORIS",
        })

        return transaksi

    # =====================================================================
    # UPDATE TRANSACTION
    # =====================================================================

    def update_transaksi(self, id: int, data: Dict[str, Any]) -> Transaksi:
        """
        Update transaction with validation.

        Args:
            id: Transaction ID
            data: Data to update

        Returns:
            Updated Transaksi instance
        """
        # Validate
        self.validator.validate_update(data)

        # Check exists
        transaksi = self.repo.get_by_id(id)
        if not transaksi:
            raise RecordNotFound("Transaksi", id)

        # Update
        return self.repo.update(id, data)

    # =====================================================================
    # FINANCIAL OPERATIONS
    # =====================================================================

    def update_financial(self, id: int, financial_data: Dict[str, Any]) -> TransaksiDetail:
        """
        Update transaction financial details (DP, subsidi, diskon, etc).

        Args:
            id: Transaction ID
            financial_data: Financial details

        Returns:
            Updated TransaksiDetail
        """
        # Validate
        self.detail_validator.validate(financial_data)

        # Check transaction exists
        transaksi = self.repo.get_by_id(id)
        if not transaksi:
            raise RecordNotFound("Transaksi", id)

        # Get OTR dari motor
        motor = transaksi.motor
        otr = float(motor.type_motor.otr or 0)

        # Validate pricing
        price_validator = PriceValidator()
        dp = float(financial_data.get("dp", 0))
        subsidi = float(financial_data.get("subsidi", 0))
        diskon = float(financial_data.get("diskon", 0))
        price_validator.validate_calculation(otr, dp, subsidi, diskon)

        # Convert date strings to date objects if needed
        if "tgl_bayar_dp" in financial_data:
            tgl = financial_data["tgl_bayar_dp"]
            if tgl and isinstance(tgl, str) and tgl.strip():
                financial_data["tgl_bayar_dp"] = datetime.strptime(tgl, "%Y-%m-%d").date()
            else:
                financial_data["tgl_bayar_dp"] = None
        if "tgl_lunas" in financial_data:
            tgl = financial_data["tgl_lunas"]
            if tgl and isinstance(tgl, str) and tgl.strip():
                financial_data["tgl_lunas"] = datetime.strptime(tgl, "%Y-%m-%d").date()
            else:
                financial_data["tgl_lunas"] = None
        if "tgl_hutang_dibayar" in financial_data:
            tgl = financial_data["tgl_hutang_dibayar"]
            if tgl and isinstance(tgl, str) and tgl.strip():
                financial_data["tgl_hutang_dibayar"] = datetime.strptime(tgl, "%Y-%m-%d").date()
            else:
                financial_data["tgl_hutang_dibayar"] = None

        # Update detail
        detail = self.detail_repo.update(id, financial_data)

        # Add catatan
        self.catatan_repo.create({
            "transaksi_id": id,
            "konten": "Financial details diperbarui",
            "tipe_catatan": "HISTORIS",
        })

        return detail

    def record_payment(self, transaksi_id: int, payment_data: Dict[str, Any]) -> Pembayaran:
        """
        Record payment for transaction.

        Args:
            transaksi_id: Transaction ID
            payment_data: Payment details

        Returns:
            Created Pembayaran record
        """
        # Check transaction exists
        transaksi = self.repo.get_by_id(transaksi_id)
        if not transaksi:
            raise RecordNotFound("Transaksi", transaksi_id)

        # Create payment record
        payment_data["transaksi_id"] = transaksi_id
        pembayaran = self.pembayaran_repo.create(payment_data)

        # Add catatan
        jumlah = payment_data.get("jumlah", 0)
        self.catatan_repo.create({
            "transaksi_id": transaksi_id,
            "konten": f"Pembayaran Rp {jumlah:,.0f} dicatat",
            "tipe_catatan": "PEMBAYARAN",
        })

        # Check if fully paid
        total_paid = self.pembayaran_repo.get_total_by_transaksi(transaksi_id)
        motor = transaksi.motor
        otr = float(motor.type_motor.otr or 0)
        detail = transaksi.detail

        if detail:
            total_diskon = float(detail.diskon_ahm or 0) + float(detail.diskon_dealer or 0) + float(detail.diskon_leasing or 0)
            due = otr - total_diskon
            if total_paid >= due:
                # Mark as paid
                self.repo.update(transaksi_id, {"status_transaksi": "L"})
                detail.tgl_lunas = date.today()
                self.catatan_repo.create({
                    "transaksi_id": transaksi_id,
                    "konten": "Transaksi lunas",
                    "tipe_catatan": "HISTORIS",
                })

        return pembayaran

    # =====================================================================
    # SEARCH & FILTER
    # =====================================================================

    def search_transaksi(
        self,
        date_from: date = None,
        date_to: date = None,
        dealer_id: int = None,
        customer_name: str = None,
        phone: str = None,
        status: str = None,
        limit: int = 100,
    ) -> List[Transaksi]:
        """
        Search transactions with multiple filters.

        Returns:
            List of matching transactions
        """
        # Default to last 30 days
        if not date_from:
            date_from = date.today() - timedelta(days=30)
        if not date_to:
            date_to = date.today()

        # Get by date range first
        transaksis = self.repo.get_by_date_range(
            date_from,
            date_to,
            dealer_id=dealer_id,
            status=status,
        )

        # Filter by customer
        if customer_name:
            transaksis = [
                t for t in transaksis
                if customer_name.lower() in t.nama_pembeli.lower()
            ]

        if phone:
            transaksis = [
                t for t in transaksis
                if phone in (t.telp_pembeli or "")
            ]

        return transaksis[:limit]

    def get_dashboard_summary(
        self,
        date_from: date = None,
        date_to: date = None,
        dealer_id: int = None,
    ) -> Dict[str, Any]:
        """
        Get dashboard summary for period.

        Returns:
            Dictionary with summary metrics
        """
        if not date_from:
            date_from = date.today() - timedelta(days=30)
        if not date_to:
            date_to = date.today()

        summary = self.repo.get_summary(date_from, date_to, dealer_id)

        return {
            "period": {
                "from": date_from.isoformat(),
                "to": date_to.isoformat(),
            },
            "transactions": {
                "total": summary["total_transaksi"],
                "total_dp": float(summary["total_dp"]),
                "total_subsidi": float(summary["total_subsidi"]),
                "total_diskon": float(summary["total_diskon"]),
                "total_insentif": float(summary["total_insentif"]),
                "total_pelunasan": float(summary["total_pelunasan"]),
            },
            "generated_at": datetime.utcnow().isoformat(),
        }

    # =====================================================================
    # TRANSACTION STATUS
    # =====================================================================

    def get_transaction_status(self, id: int) -> Dict[str, Any]:
        """Get detailed transaction status"""
        transaksi = self.repo.get_by_id(id)
        if not transaksi:
            raise RecordNotFound("Transaksi", id)

        motor = transaksi.motor
        otr = float(motor.type_motor.otr or 0)
        detail = transaksi.detail

        total_diskon = 0
        total_dp = 0
        if detail:
            total_diskon = float(detail.diskon_ahm or 0) + float(detail.diskon_dealer or 0) + float(detail.diskon_leasing or 0)
            total_dp = float(detail.dp or 0)

        due_amount = otr - total_diskon

        # Get payments
        payments = self.pembayaran_repo.get_by_transaksi(id)
        total_paid = sum(float(p.jumlah) for p in payments)

        remaining = max(0, due_amount - total_paid)

        return {
            "nota": transaksi.nota,
            "status": transaksi.status_transaksi,
            "customer": transaksi.nama_pembeli,
            "motor": {
                "no_mesin": motor.no_mesin,
                "type": motor.type_motor.nama_type,
            },
            "financial": {
                "otr": otr,
                "discount": total_diskon,
                "due": due_amount,
                "dp_received": total_dp,
                "total_paid": total_paid,
                "remaining": remaining,
            },
            "payments": len(payments),
        }

    # =====================================================================
    # NOTES & DOCUMENTS
    # =====================================================================

    def add_note(self, transaksi_id: int, content: str, note_type: str = "HISTORIS") -> Catatan:
        """Add note to transaction"""
        transaksi = self.repo.get_by_id(transaksi_id)
        if not transaksi:
            raise RecordNotFound("Transaksi", transaksi_id)

        return self.catatan_repo.create({
            "transaksi_id": transaksi_id,
            "konten": content,
            "tipe_catatan": note_type,
        })

    def get_notes(self, transaksi_id: int) -> List[Catatan]:
        """Get all notes for transaction"""
        return self.catatan_repo.get_by_transaksi(transaksi_id)

    # =====================================================================
    # DELETE/CANCEL
    # =====================================================================

    def cancel_transaksi(self, id: int, reason: str = "") -> bool:
        """
        Cancel transaction.

        Args:
            id: Transaction ID
            reason: Cancellation reason

        Returns:
            True if successful
        """
        transaksi = self.repo.get_by_id(id)
        if not transaksi:
            raise RecordNotFound("Transaksi", id)

        # Can only cancel if not paid
        if transaksi.status_transaksi == "L":
            raise FinancialException("Tidak bisa membatalkan transaksi yang sudah lunas")

        # Update status
        self.repo.update(id, {"status_transaksi": "C"})

        # Restore motor status
        self.motor_repo.update(
            transaksi.motor_id,
            {"status": "R", "tgl_status": datetime.utcnow()}
        )

        # Add note
        self.catatan_repo.create({
            "transaksi_id": id,
            "konten": f"Transaksi dibatalkan. Alasan: {reason}",
            "tipe_catatan": "HISTORIS",
        })

        return True


class DealerService:
    """Service for dealer management"""

    def __init__(self):
        self.repo = DealerRepository()

    def get_all(self) -> List:
        """Get all dealers"""
        return self.repo.get_all()

    def get_active(self) -> List:
        """Get active dealers"""
        return self.repo.get_active()

    def get_with_sales(self) -> List:
        """Get dealers that have sales"""
        return self.repo.get_with_transactions()

    def get_sales_by_dealer(self, dealer_id: int, days: int = 30) -> Dict[str, Any]:
        """Get sales statistics for dealer"""
        dealer = self.repo.get_by_id(dealer_id)
        if not dealer:
            raise RecordNotFound("Dealer", dealer_id)

        transaksi_service = TransaksiService()
        date_from = date.today() - timedelta(days=days)
        date_to = date.today()

        summary = transaksi_service.get_dashboard_summary(
            date_from=date_from,
            date_to=date_to,
            dealer_id=dealer_id,
        )

        return {
            "dealer": dealer.nama,
            **summary,
        }


class StokService:
    """Service for inventory management"""

    def __init__(self):
        self.repo = StokMotorRepository()
        self.validator = StokMotorValidator()

    def get_ready_stock(self) -> List:
        """Get ready-for-sale vehicles"""
        return self.repo.get_ready()

    def get_status_summary(self) -> Dict[str, int]:
        """Get vehicle count by status"""
        return self.repo.count_by_status()

    def get_by_type(self, type_id: int) -> List:
        """Get vehicles by type"""
        return self.repo.get_by_type(type_id)

    def get_by_dealer(self, dealer_id: int) -> List:
        """Get vehicles by dealer"""
        return self.repo.get_by_dealer(dealer_id)


class ReportService:
    """Service for generating reports"""

    def __init__(self):
        self.transaksi_service = TransaksiService()
        self.dealer_repo = DealerRepository()

    def get_monthly_summary(self, year: int, month: int) -> Dict[str, Any]:
        """Get monthly report"""
        date_from = date(year, month, 1)
        # Get last day of month
        if month == 12:
            date_to = date(year + 1, 1, 1) - timedelta(days=1)
        else:
            date_to = date(year, month + 1, 1) - timedelta(days=1)

        summary = self.transaksi_service.get_dashboard_summary(date_from, date_to)

        # Add dealer breakdown
        dealers = self.dealer_repo.get_all()
        dealer_summaries = []

        for dealer in dealers:
            dealer_summary = self.transaksi_service.get_dashboard_summary(
                date_from, date_to, dealer.id
            )
            if dealer_summary["transactions"]["total"] > 0:
                dealer_summaries.append({
                    "dealer": dealer.nama,
                    **dealer_summary,
                })

        return {
            "month": f"{year}-{month:02d}",
            "overall": summary,
            "by_dealer": dealer_summaries,
        }

    def get_quarterly_summary(self, year: int, quarter: int) -> Dict[str, Any]:
        """Get quarterly report"""
        month_start = (quarter - 1) * 3 + 1
        month_end = quarter * 3

        date_from = date(year, month_start, 1)
        if month_end == 12:
            date_to = date(year + 1, 1, 1) - timedelta(days=1)
        else:
            date_to = date(year, month_end + 1, 1) - timedelta(days=1)

        return self.transaksi_service.get_dashboard_summary(date_from, date_to)
