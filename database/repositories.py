"""
Concrete Repository Implementations
Each repository handles specific model operations
"""

from typing import List, Optional, Dict, Any
from datetime import date, datetime

from database.repository import BaseRepository
from database.connection import DatabaseManager
from database.models import (
    Transaksi,
    TransaksiDetail,
    Dealer,
    Broker,
    Leasing,
    TypeMotor,
    StokMotor,
    Dokumen,
    Catatan,
    Pembayaran,
)


class TransaksiRepository(BaseRepository[Transaksi]):
    """Repository for Transaksi (Transactions)"""

    def __init__(self):
        super().__init__(Transaksi)

    def get_by_nota(self, nota: str) -> Optional[Transaksi]:
        """Get transaction by nota (transaction number)"""
        session = self.get_session()
        # DO NOT close session - let Flask's app context handle it
        return session.query(Transaksi).filter(
            Transaksi.nota == nota
        ).first()

    def get_by_date_range(
        self,
        date_from: date,
        date_to: date,
        dealer_id: int = None,
        status: str = None,
    ) -> List[Transaksi]:
        """
        Get transactions by date range with optional filters.

        Args:
            date_from: Start date
            date_to: End date
            dealer_id: Optional dealer filter
            status: Optional status filter (P, A, L, C)

        Returns:
            List of transactions
        """
        session = self.get_session()
        # DO NOT close session - let Flask's app context handle session lifecycle
        # This prevents lazy-load errors when accessing relationships after query
        query = session.query(Transaksi).filter(
            Transaksi.tanggal.between(date_from, date_to)
        )

        if dealer_id:
            query = query.filter(Transaksi.dealer_id == dealer_id)

        if status:
            query = query.filter(Transaksi.status_transaksi == status)

        return query.order_by(Transaksi.tanggal.desc()).all()

    def search_by_customer(self, search_term: str) -> List[Transaksi]:
        """
        Search transactions by customer name or phone.

        Args:
            search_term: Name or phone number to search

        Returns:
            List of matching transactions
        """
        session = self.get_session()
        # DO NOT close session - let Flask's app context handle it
        return session.query(Transaksi).filter(
            (Transaksi.nama_pembeli.ilike(f"%{search_term}%")) |
            (Transaksi.telp_pembeli.ilike(f"%{search_term}%"))
        ).all()

    def get_by_dealer(self, dealer_id: int, limit: int = 100) -> List[Transaksi]:
        """Get transactions by dealer"""
        return self.filter(dealer_id=dealer_id)[:limit]

    def get_by_leasing(self, leasing_id: int) -> List[Transaksi]:
        """Get transactions by leasing company"""
        return self.filter(leasing_id=leasing_id)

    def get_by_status(self, status: str) -> List[Transaksi]:
        """Get transactions by status (P, A, L, C)"""
        return self.filter(status_transaksi=status)

    def get_unpaid(self) -> List[Transaksi]:
        """Get unpaid transactions (status != L)"""
        session = self.get_session()
        # DO NOT close session - let Flask's app context handle it
        return session.query(Transaksi).filter(
            Transaksi.status_transaksi != "L"
        ).all()

    def get_summary(
        self,
        date_from: date,
        date_to: date,
        dealer_id: int = None,
    ) -> Dict[str, Any]:
        """
        Get summary statistics for transactions.

        Returns:
            Dictionary with totals and counts
        """
        session = self.get_session()
        try:
            query = session.query(Transaksi).filter(
                Transaksi.tanggal.between(date_from, date_to)
            )

            if dealer_id:
                query = query.filter(Transaksi.dealer_id == dealer_id)

            transaksis = query.all()

            # Calculate totals
            total_dp = 0
            total_subsidi = 0
            total_diskon = 0
            total_insentif = 0
            total_pelunasan = 0

            for t in transaksis:
                if t.detail:
                    total_dp += float(t.detail.dp or 0)
                    total_subsidi += float(t.detail.subsidi or 0)
                    total_diskon += float(
                        (t.detail.diskon_ahm or 0) + (t.detail.diskon_dealer or 0) + (t.detail.diskon_leasing or 0)
                    )
                    total_insentif += float(t.detail.insentif or 0)
                    total_pelunasan += float(t.detail.pelunasan or 0)

            return {
                "total_transaksi": len(transaksis),
                "total_dp": total_dp,
                "total_subsidi": total_subsidi,
                "total_diskon": total_diskon,
                "total_insentif": total_insentif,
                "total_pelunasan": total_pelunasan,
            }
        finally:
            session.close()


class TransaksiDetailRepository(BaseRepository[TransaksiDetail]):
    """Repository for TransaksiDetail (Financial details)"""

    def __init__(self):
        super().__init__(TransaksiDetail)

    def get_by_transaksi(self, transaksi_id: int) -> Optional[TransaksiDetail]:
        """Get detail by transaction ID"""
        return self.get_by_id(transaksi_id)


class DealerRepository(BaseRepository[Dealer]):
    """Repository for Dealer (Dealers/Branches)"""

    def __init__(self):
        super().__init__(Dealer)

    def get_by_name(self, nama: str) -> Optional[Dealer]:
        """Get dealer by name"""
        session = self.get_session()
        try:
            return session.query(Dealer).filter(
                Dealer.nama == nama
            ).first()
        finally:
            session.close()

    def get_active(self) -> List[Dealer]:
        """Get all active dealers"""
        return self.filter(status="A")

    def search_by_city(self, kota: str) -> List[Dealer]:
        """Search dealers by city"""
        return self.filter_like("kota", kota)

    def get_with_transactions(self) -> List[Dealer]:
        """Get dealers that have transactions"""
        session = self.get_session()
        try:
            return session.query(Dealer).filter(
                Dealer.transaksis.any()
            ).all()
        finally:
            session.close()


class BrokerRepository(BaseRepository[Broker]):
    """Repository for Broker (Brokers/Intermediaries)"""

    def __init__(self):
        super().__init__(Broker)

    def get_by_name(self, nama: str) -> Optional[Broker]:
        """Get broker by name"""
        session = self.get_session()
        try:
            return session.query(Broker).filter(
                Broker.nama == nama
            ).first()
        finally:
            session.close()

    def get_active(self) -> List[Broker]:
        """Get all active brokers"""
        return self.filter(status="A")

    def get_by_type(self, tipe: str) -> List[Broker]:
        """Get brokers by type (B=Broker, L=Leasing Partner)"""
        return self.filter(tipe=tipe)


class LeasingRepository(BaseRepository[Leasing]):
    """Repository for Leasing (Leasing Companies)"""

    def __init__(self):
        super().__init__(Leasing)

    def get_by_kode(self, kode: str) -> Optional[Leasing]:
        """Get leasing by code"""
        session = self.get_session()
        try:
            return session.query(Leasing).filter(
                Leasing.kode == kode
            ).first()
        finally:
            session.close()

    def get_active(self) -> List[Leasing]:
        """Get all active leasing companies"""
        return self.filter(status="A")

    def get_by_name(self, nama: str) -> Optional[Leasing]:
        """Get leasing by name"""
        session = self.get_session()
        try:
            return session.query(Leasing).filter(
                Leasing.nama == nama
            ).first()
        finally:
            session.close()


class TypeMotorRepository(BaseRepository[TypeMotor]):
    """Repository for TypeMotor (Motor Types/Models)"""

    def __init__(self):
        super().__init__(TypeMotor)

    def get_by_kode(self, kode_type: str) -> Optional[TypeMotor]:
        """Get motor type by code"""
        session = self.get_session()
        try:
            return session.query(TypeMotor).filter(
                TypeMotor.kode_type == kode_type
            ).first()
        finally:
            session.close()

    def get_active(self) -> List[TypeMotor]:
        """Get all active motor types"""
        return self.filter(status="A")

    def get_by_merek(self, merek: str) -> List[TypeMotor]:
        """Get motor types by brand"""
        return self.filter(merek=merek)

    def search_by_name(self, nama: str) -> List[TypeMotor]:
        """Search motor types by name"""
        return self.filter_like("nama_type", nama)

    def get_by_cc_range(self, cc_min: int, cc_max: int) -> List[TypeMotor]:
        """Get motor types by engine size range"""
        session = self.get_session()
        try:
            return session.query(TypeMotor).filter(
                TypeMotor.cc.between(cc_min, cc_max)
            ).all()
        finally:
            session.close()


class StokMotorRepository(BaseRepository[StokMotor]):
    """Repository for StokMotor (Vehicle Inventory)"""

    def __init__(self):
        super().__init__(StokMotor)

    def get_by_no_mesin(self, no_mesin: str) -> Optional[StokMotor]:
        """Get vehicle by engine number"""
        session = self.get_session()
        try:
            return session.query(StokMotor).filter(
                StokMotor.no_mesin == no_mesin
            ).first()
        finally:
            session.close()

    def get_by_no_rangka(self, no_rangka: str) -> Optional[StokMotor]:
        """Get vehicle by chassis number"""
        session = self.get_session()
        try:
            return session.query(StokMotor).filter(
                StokMotor.no_rangka == no_rangka
            ).first()
        finally:
            session.close()

    def get_ready(self) -> List[StokMotor]:
        """Get all ready-for-sale vehicles"""
        return self.filter(status="R")

    def get_sold(self) -> List[StokMotor]:
        """Get all sold vehicles"""
        return self.filter(status="S")

    def get_by_type(self, type_id: int) -> List[StokMotor]:
        """Get vehicles by type"""
        return self.filter(type_id=type_id)

    def get_by_dealer(self, dealer_id: int) -> List[StokMotor]:
        """Get vehicles by dealer"""
        return self.filter(dealer_id=dealer_id)

    def get_by_dealer_and_status(
        self,
        dealer_id: int,
        status: str,
    ) -> List[StokMotor]:
        """Get vehicles by dealer and status"""
        session = self.get_session()
        try:
            return session.query(StokMotor).filter(
                (StokMotor.dealer_id == dealer_id) &
                (StokMotor.status == status)
            ).all()
        finally:
            session.close()

    def get_by_color(self, warna: str) -> List[StokMotor]:
        """Get vehicles by color"""
        return self.filter_like("warna", warna)

    def get_arrived_between(
        self,
        date_from: date,
        date_to: date,
    ) -> List[StokMotor]:
        """Get vehicles arrived in date range"""
        return self.filter_between("tgl_datang", date_from, date_to)

    def count_by_status(self) -> Dict[str, int]:
        """Get count of vehicles by status"""
        session = self.get_session()
        try:
            statuses = ["R", "S", "T", "D"]
            result = {}

            for status in statuses:
                count = session.query(StokMotor).filter(
                    StokMotor.status == status
                ).count()
                result[status] = count

            return result
        finally:
            session.close()


class DokumenRepository(BaseRepository[Dokumen]):
    """Repository for Dokumen (Transaction Documents)"""

    def __init__(self):
        super().__init__(Dokumen)

    def get_by_transaksi(self, transaksi_id: int) -> List[Dokumen]:
        """Get all documents for a transaction"""
        return self.filter(transaksi_id=transaksi_id)

    def get_by_type(self, tipe_dokumen: str) -> List[Dokumen]:
        """Get documents by type"""
        return self.filter(tipe_dokumen=tipe_dokumen)

    def get_bpkb(self, transaksi_id: int) -> Optional[Dokumen]:
        """Get BPKB document for transaction"""
        session = self.get_session()
        try:
            return session.query(Dokumen).filter(
                (Dokumen.transaksi_id == transaksi_id) &
                (Dokumen.tipe_dokumen == "BPKB")
            ).first()
        finally:
            session.close()

    def get_expired_docs(self) -> List[Dokumen]:
        """Get expired documents"""
        session = self.get_session()
        try:
            today = date.today()
            return session.query(Dokumen).filter(
                Dokumen.tgl_berlaku < today
            ).all()
        finally:
            session.close()


class CatatanRepository(BaseRepository[Catatan]):
    """Repository for Catatan (Historical Notes)"""

    def __init__(self):
        super().__init__(Catatan)

    def get_by_transaksi(self, transaksi_id: int) -> List[Catatan]:
        """Get all notes for a transaction"""
        session = self.get_session()
        try:
            return session.query(Catatan).filter(
                Catatan.transaksi_id == transaksi_id
            ).order_by(Catatan.tgl_catatan.desc()).all()
        finally:
            session.close()

    def get_by_type(self, tipe_catatan: str) -> List[Catatan]:
        """Get notes by type"""
        return self.filter(tipe_catatan=tipe_catatan)

    def get_recent(self, days: int = 7) -> List[Catatan]:
        """Get notes from last N days"""
        session = self.get_session()
        try:
            from datetime import timedelta

            cutoff_date = datetime.utcnow() - timedelta(days=days)
            return session.query(Catatan).filter(
                Catatan.tgl_catatan >= cutoff_date
            ).order_by(Catatan.tgl_catatan.desc()).all()
        finally:
            session.close()


class PembayaranRepository(BaseRepository[Pembayaran]):
    """Repository for Pembayaran (Payment Records)"""

    def __init__(self):
        super().__init__(Pembayaran)

    def get_by_transaksi(self, transaksi_id: int) -> List[Pembayaran]:
        """Get all payments for a transaction"""
        session = self.get_session()
        try:
            return session.query(Pembayaran).filter(
                Pembayaran.transaksi_id == transaksi_id
            ).order_by(Pembayaran.tgl_pembayaran).all()
        finally:
            session.close()

    def get_pending(self) -> List[Pembayaran]:
        """Get pending payments"""
        return self.filter(status="P")

    def get_by_date_range(
        self,
        date_from: date,
        date_to: date,
    ) -> List[Pembayaran]:
        """Get payments in date range"""
        return self.filter_between("tgl_pembayaran", date_from, date_to)

    def get_total_by_transaksi(self, transaksi_id: int) -> float:
        """Get total amount paid for transaction"""
        session = self.get_session()
        try:
            result = session.query(
                __import__('sqlalchemy').func.sum(Pembayaran.jumlah)
            ).filter(
                Pembayaran.transaksi_id == transaksi_id
            ).scalar()

            return float(result or 0)
        finally:
            session.close()
