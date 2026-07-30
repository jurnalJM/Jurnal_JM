"""
Unit Tests for Services
Tests business logic and workflows
"""

import pytest
from datetime import date, timedelta

from database.connection import DatabaseManager
from database.models import Base
from database.repositories import (
    TransaksiRepository,
    StokMotorRepository,
    DealerRepository,
)
from business.services import (
    TransaksiService,
    DealerService,
    StokService,
    ReportService,
)
from business.validators import (
    TransaksiValidator,
    PriceValidator,
)
from business.exceptions import (
    RecordNotFound,
    InventoryException,
    ValidationErrors,
    FinancialException,
)


@pytest.fixture(scope="module")
def test_db_with_data():
    """Setup test database with data"""
    test_db_url = "sqlite:///:memory:"

    DatabaseManager.initialize(test_db_url)
    Base.metadata.create_all(DatabaseManager.get_engine())

    from database.schema import seed_master_data
    with DatabaseManager.session_context() as session:
        seed_master_data()

    yield test_db_url

    DatabaseManager.drop_all_tables()
    DatabaseManager.close_all_connections()


# =====================================================================
# TRANSAKSI VALIDATOR TESTS
# =====================================================================

class TestTransaksiValidator:
    """Test TransaksiValidator"""

    def test_validate_required_fields(self):
        """Test required field validation"""
        validator = TransaksiValidator()

        # Missing nota
        data = {
            "tanggal": date.today(),
            "dealer_id": 1,
            "nama_pembeli": "Test",
            "motor_id": 1,
        }

        with pytest.raises(ValidationErrors):
            validator.validate_create(data)

    def test_validate_nota_format(self):
        """Test nota format validation"""
        validator = TransaksiValidator()

        data = {
            "nota": "invalid-nota!",
            "tanggal": date.today(),
            "dealer_id": 1,
            "nama_pembeli": "Test",
            "motor_id": 1,
        }

        with pytest.raises(ValidationErrors):
            validator.validate_create(data)

    def test_validate_success(self):
        """Test successful validation"""
        validator = TransaksiValidator()

        data = {
            "nota": "TRX-TEST-001",
            "tanggal": date.today(),
            "dealer_id": 1,
            "nama_pembeli": "Test User",
            "motor_id": 1,
        }

        # Should not raise
        result = validator.validate_create(data)
        assert result is True


class TestPriceValidator:
    """Test PriceValidator"""

    def test_validate_dp_exceeds_otr(self):
        """Test DP validation"""
        validator = PriceValidator()

        with pytest.raises(ValidationErrors):
            validator.validate_calculation(
                otr=100000,
                dp=150000,  # Exceeds OTR
                subsidi=0,
                diskon=0,
            )

    def test_validate_discount_exceeds_otr(self):
        """Test discount validation"""
        validator = PriceValidator()

        with pytest.raises(ValidationErrors):
            validator.validate_calculation(
                otr=100000,
                dp=0,
                subsidi=60000,
                diskon=50000,  # Total 110000 > OTR
            )

    def test_validate_success(self):
        """Test successful price validation"""
        validator = PriceValidator()

        result = validator.validate_calculation(
            otr=100000000,
            dp=20000000,
            subsidi=5000000,
            diskon=10000000,
        )

        assert result is True


# =====================================================================
# TRANSAKSI SERVICE TESTS
# =====================================================================

class TestTransaksiService:
    """Test TransaksiService"""

    def test_create_transaksi_success(self, test_db_with_data):
        """Test successful transaction creation"""
        service = TransaksiService()

        data = {
            "nota": "SVC-TEST-001",
            "tanggal": date.today(),
            "dealer_id": 1,
            "nama_pembeli": "Service Test User",
            "motor_id": 1,
        }

        transaksi = service.create_transaksi(data)

        assert transaksi.id is not None
        assert transaksi.nota == "SVC-TEST-001"
        assert transaksi.status_transaksi == "P"  # Pending
        assert transaksi.detail is not None

    def test_create_transaksi_motor_not_found(self, test_db_with_data):
        """Test creating transaction with non-existent motor"""
        service = TransaksiService()

        data = {
            "nota": "SVC-TEST-002",
            "tanggal": date.today(),
            "dealer_id": 1,
            "nama_pembeli": "Test User",
            "motor_id": 99999,  # Non-existent
        }

        with pytest.raises(RecordNotFound):
            service.create_transaksi(data)

    def test_create_transaksi_dealer_not_found(self, test_db_with_data):
        """Test creating transaction with non-existent dealer"""
        service = TransaksiService()

        data = {
            "nota": "SVC-TEST-003",
            "tanggal": date.today(),
            "dealer_id": 99999,  # Non-existent
            "nama_pembeli": "Test User",
            "motor_id": 1,
        }

        with pytest.raises(RecordNotFound):
            service.create_transaksi(data)

    def test_update_transaksi(self, test_db_with_data):
        """Test updating transaction"""
        service = TransaksiService()

        # Create first
        data = {
            "nota": "SVC-TEST-004",
            "tanggal": date.today(),
            "dealer_id": 1,
            "nama_pembeli": "Initial Name",
            "motor_id": 1,
        }
        transaksi = service.create_transaksi(data)

        # Update
        updated = service.update_transaksi(
            transaksi.id,
            {"nama_pembeli": "Updated Name"}
        )

        assert updated.nama_pembeli == "Updated Name"

    def test_update_financial(self, test_db_with_data):
        """Test updating financial details"""
        service = TransaksiService()

        # Create transaction
        data = {
            "nota": "SVC-TEST-005",
            "tanggal": date.today(),
            "dealer_id": 1,
            "nama_pembeli": "Test User",
            "motor_id": 1,
        }
        transaksi = service.create_transaksi(data)

        # Update financial
        detail = service.update_financial(
            transaksi.id,
            {
                "dp": 5000000,
                "subsidi": 2000000,
                "diskon": 1000000,
                "insentif": 500000,
            }
        )

        assert float(detail.dp) == 5000000
        assert float(detail.subsidi) == 2000000

    def test_record_payment(self, test_db_with_data):
        """Test recording payment"""
        service = TransaksiService()

        # Create transaction
        data = {
            "nota": "SVC-TEST-006",
            "tanggal": date.today(),
            "dealer_id": 1,
            "nama_pembeli": "Test User",
            "motor_id": 1,
        }
        transaksi = service.create_transaksi(data)

        # Record payment
        payment = service.record_payment(
            transaksi.id,
            {
                "tgl_pembayaran": date.today(),
                "jumlah": 5000000,
                "tipe_pembayaran": "DP",
                "metode": "TUNAI",
            }
        )

        assert payment.jumlah == 5000000

    def test_search_transaksi(self, test_db_with_data):
        """Test searching transactions"""
        service = TransaksiService()

        # Create multiple
        for i in range(3):
            service.create_transaksi({
                "nota": f"SEARCH-{i}",
                "tanggal": date.today(),
                "dealer_id": 1,
                "nama_pembeli": f"Customer {i}",
                "motor_id": 1,
            })

        # Search by customer
        results = service.search_transaksi(customer_name="Customer")
        assert len(results) >= 3

    def test_get_dashboard_summary(self, test_db_with_data):
        """Test getting dashboard summary"""
        service = TransaksiService()

        # Create transaction with financial details
        transaksi = service.create_transaksi({
            "nota": "SUMMARY-TEST",
            "tanggal": date.today(),
            "dealer_id": 1,
            "nama_pembeli": "Test User",
            "motor_id": 1,
        })

        service.update_financial(
            transaksi.id,
            {
                "dp": 10000000,
                "subsidi": 5000000,
                "diskon": 2000000,
            }
        )

        # Get summary
        summary = service.get_dashboard_summary()

        assert "transactions" in summary
        assert summary["transactions"]["total_transaksi"] >= 1

    def test_get_transaction_status(self, test_db_with_data):
        """Test getting transaction status"""
        service = TransaksiService()

        transaksi = service.create_transaksi({
            "nota": "STATUS-TEST",
            "tanggal": date.today(),
            "dealer_id": 1,
            "nama_pembeli": "Test User",
            "motor_id": 1,
        })

        status = service.get_transaction_status(transaksi.id)

        assert "nota" in status
        assert "status" in status
        assert "financial" in status

    def test_add_note(self, test_db_with_data):
        """Test adding note to transaction"""
        service = TransaksiService()

        transaksi = service.create_transaksi({
            "nota": "NOTE-TEST",
            "tanggal": date.today(),
            "dealer_id": 1,
            "nama_pembeli": "Test User",
            "motor_id": 1,
        })

        note = service.add_note(transaksi.id, "Test note content")

        assert note.konten == "Test note content"

    def test_get_notes(self, test_db_with_data):
        """Test getting transaction notes"""
        service = TransaksiService()

        transaksi = service.create_transaksi({
            "nota": "NOTES-TEST",
            "tanggal": date.today(),
            "dealer_id": 1,
            "nama_pembeli": "Test User",
            "motor_id": 1,
        })

        service.add_note(transaksi.id, "Note 1")
        service.add_note(transaksi.id, "Note 2")

        notes = service.get_notes(transaksi.id)

        assert len(notes) >= 2  # At least 2 (plus initial note)

    def test_cancel_transaksi(self, test_db_with_data):
        """Test cancelling transaction"""
        service = TransaksiService()

        transaksi = service.create_transaksi({
            "nota": "CANCEL-TEST",
            "tanggal": date.today(),
            "dealer_id": 1,
            "nama_pembeli": "Test User",
            "motor_id": 1,
        })

        result = service.cancel_transaksi(transaksi.id, "Test cancellation")

        assert result is True

        # Verify status changed
        updated = service.repo.get_by_id(transaksi.id)
        assert updated.status_transaksi == "C"


# =====================================================================
# DEALER SERVICE TESTS
# =====================================================================

class TestDealerService:
    """Test DealerService"""

    def test_get_all_dealers(self, test_db_with_data):
        """Test getting all dealers"""
        service = DealerService()
        dealers = service.get_all()

        assert len(dealers) >= 3

    def test_get_active_dealers(self, test_db_with_data):
        """Test getting active dealers"""
        service = DealerService()
        dealers = service.get_active()

        assert len(dealers) >= 3
        assert all(d.status == "A" for d in dealers)


# =====================================================================
# STOK SERVICE TESTS
# =====================================================================

class TestStokService:
    """Test StokService"""

    def test_get_ready_stock(self, test_db_with_data):
        """Test getting ready vehicles"""
        service = StokService()
        ready = service.get_ready_stock()

        assert len(ready) >= 0

    def test_get_status_summary(self, test_db_with_data):
        """Test getting status summary"""
        service = StokService()
        summary = service.get_status_summary()

        assert isinstance(summary, dict)
        assert all(status in summary for status in ["R", "S", "T", "D"])


# =====================================================================
# REPORT SERVICE TESTS
# =====================================================================

class TestReportService:
    """Test ReportService"""

    def test_get_monthly_summary(self, test_db_with_data):
        """Test getting monthly report"""
        service = ReportService()
        today = date.today()

        report = service.get_monthly_summary(today.year, today.month)

        assert "month" in report
        assert "overall" in report
        assert "by_dealer" in report

    def test_get_quarterly_summary(self, test_db_with_data):
        """Test getting quarterly report"""
        service = ReportService()
        today = date.today()
        quarter = (today.month - 1) // 3 + 1

        report = service.get_quarterly_summary(today.year, quarter)

        assert "period" in report
        assert "transactions" in report


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
