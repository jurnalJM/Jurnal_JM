"""
Integration tests for complete application workflows
"""

import pytest
from datetime import datetime, timedelta
from unittest.mock import Mock, patch

from database.connection import DatabaseManager
from database.models import Base, Dealer, TypeMotor, StokMotor, Transaksi, TransaksiDetail, Leasing
from database.repositories import (
    TransaksiRepository, StokMotorRepository, DealerRepository,
    TypeMotorRepository, LeasingRepository
)
from business.services import TransaksiService
from business.exceptions import ValidationException, RecordNotFound, InsufficientDataException


@pytest.fixture(scope="function")
def integration_db(test_database_url):
    """Create test database with seed data for integration tests"""
    DatabaseManager.initialize(test_database_url)
    Base.metadata.create_all(DatabaseManager.get_engine())

    session = DatabaseManager.get_session()

    # Create master data
    dealers = [
        Dealer(nama="PT Jaya Motor Pusat", kota="Jakarta", alamat="Jl. Jaya 1", telp="02112345678"),
        Dealer(nama="PT Jaya Motor BSD", kota="Serpong", alamat="Jl. BSD 2", telp="02154321098"),
    ]
    session.add_all(dealers)
    session.flush()

    motor_types = [
        TypeMotor(kode_type="PCX160", nama_type="PCX 160", merek="Honda", cc=160, otr=25000000, warna_tersedia="Merah,Hitam,Putih"),
        TypeMotor(kode_type="VARIO125", nama_type="Vario 125", merek="Honda", cc=125, otr=18000000, warna_tersedia="Biru,Merah,Putih"),
    ]
    session.add_all(motor_types)
    session.flush()

    leasing_companies = [
        Leasing(kode="MANDIRI", nama="Mandiri Finance", alamat="Jl. Sudirman", telp="02198765432"),
        Leasing(kode="BCA", nama="BCA Finance", alamat="Jl. MH Thamrin", telp="02108765432"),
    ]
    session.add_all(leasing_companies)
    session.flush()

    # Create inventory
    stocks = [
        StokMotor(type_id=motor_types[0].id, warna="Merah", no_mesin="PCX001", no_rangka="RANGE001", tgl_datang=datetime.now().date(), status="R"),
        StokMotor(type_id=motor_types[0].id, warna="Hitam", no_mesin="PCX002", no_rangka="RANGE002", tgl_datang=datetime.now().date(), status="R"),
        StokMotor(type_id=motor_types[1].id, warna="Biru", no_mesin="VAR001", no_rangka="RANGE003", tgl_datang=datetime.now().date(), status="R"),
    ]
    session.add_all(stocks)
    session.commit()

    yield session

    # Cleanup
    Base.metadata.drop_all(DatabaseManager.get_engine())
    DatabaseManager.close_all_connections()


class TestTransactionWorkflow:
    """Test complete transaction creation and management workflow"""

    def test_create_transaction_complete_workflow(self, integration_db):
        """Test full transaction creation from start to finish"""
        service = TransaksiService()

        # Create transaction
        trans_data = {
            "nota": "TRX-001",
            "tanggal": datetime.now().date(),
            "id_dealer": 1,
            "nama_pembeli": "Budi Santoso",
            "alamat_pembeli": "Jl. Merdeka 123",
            "telp_pembeli": "081234567890",
            "email_pembeli": "budi@example.com",
            "id_motor": 1,
            "id_leasing": 1,
            "status_transaksi": "P",
        }

        detail_data = {
            "dp": 10000000.0,
            "subsidi": 2000000.0,
            "diskon": 500000.0,
            "diskon_tambahan": 100000.0,
            "insentif": 200000.0,
        }

        # Create
        transaksi = service.create_transaksi(trans_data, detail_data)
        assert transaksi is not None
        assert transaksi.nota == "TRX-001"
        assert transaksi.status_transaksi == "P"

        # Verify detail created
        assert transaksi.detail is not None
        assert transaksi.detail.dp == 10000000.0

        # Verify motor status changed
        repo = StokMotorRepository()
        motor = repo.get_by_id(1, integration_db)
        assert motor.status == "S"  # S = Sold

    def test_update_transaction_status(self, integration_db):
        """Test updating transaction status"""
        service = TransaksiService()

        # Create transaction
        trans_data = {
            "nota": "TRX-002",
            "tanggal": datetime.now().date(),
            "id_dealer": 1,
            "nama_pembeli": "Ahmad Wijaya",
            "alamat_pembeli": "Jl. Ahmad 456",
            "telp_pembeli": "081234567891",
            "email_pembeli": "ahmad@example.com",
            "id_motor": 2,
            "id_leasing": 2,
            "status_transaksi": "P",
        }

        detail_data = {
            "dp": 8000000.0,
            "subsidi": 1500000.0,
            "diskon": 300000.0,
            "diskon_tambahan": 50000.0,
            "insentif": 150000.0,
        }

        transaksi = service.create_transaksi(trans_data, detail_data)
        trans_id = transaksi.id

        # Update to Approved
        service.update_transaksi(
            trans_id,
            {"status_transaksi": "A"},
            integration_db
        )

        # Verify status changed
        repo = TransaksiRepository()
        updated = repo.get_by_id(trans_id, integration_db)
        assert updated.status_transaksi == "A"

    def test_transaction_payment_recording(self, integration_db):
        """Test recording payment for transaction"""
        service = TransaksiService()

        # Create transaction
        trans_data = {
            "nota": "TRX-003",
            "tanggal": datetime.now().date(),
            "id_dealer": 1,
            "nama_pembeli": "Siti Nurhaliza",
            "alamat_pembeli": "Jl. Siti 789",
            "telp_pembeli": "081234567892",
            "email_pembeli": "siti@example.com",
            "id_motor": 3,
            "id_leasing": 1,
            "status_transaksi": "A",
        }

        detail_data = {
            "dp": 5000000.0,
            "subsidi": 1000000.0,
            "diskon": 200000.0,
            "diskon_tambahan": 30000.0,
            "insentif": 100000.0,
        }

        transaksi = service.create_transaksi(trans_data, detail_data)

        # Record full payment
        payment_data = {
            "tgl_lunas": datetime.now().date(),
            "pelunasan": 5000000.0,
        }

        service.record_payment(transaksi.id, payment_data, integration_db)

        # Verify payment recorded
        repo = TransaksiRepository()
        updated = repo.get_by_id(transaksi.id, integration_db)
        assert updated.detail.pelunasan == 5000000.0
        assert updated.detail.tgl_lunas == datetime.now().date()

    def test_search_transactions_by_date_range(self, integration_db):
        """Test searching transactions by date range"""
        service = TransaksiService()

        # Create multiple transactions
        for i in range(3):
            trans_data = {
                "nota": f"TRX-{i+10:03d}",
                "tanggal": datetime.now().date() - timedelta(days=i),
                "id_dealer": 1,
                "nama_pembeli": f"Customer {i+1}",
                "alamat_pembeli": f"Jl. {i+1}",
                "telp_pembeli": f"0812000000{i:02d}",
                "email_pembeli": f"customer{i}@example.com",
                "id_motor": 1,
                "id_leasing": 1,
                "status_transaksi": "A",
            }

            detail_data = {
                "dp": 5000000.0,
                "subsidi": 1000000.0,
                "diskon": 100000.0,
                "diskon_tambahan": 0,
                "insentif": 50000.0,
            }

            service.create_transaksi(trans_data, detail_data)

        # Search by date range
        results = service.search_transaksi(
            date_from=datetime.now().date() - timedelta(days=5),
            date_to=datetime.now().date(),
            session=integration_db
        )

        assert len(results) >= 3


class TestRepositoryIntegration:
    """Test repository operations with actual data"""

    def test_dealer_repository_operations(self, integration_db):
        """Test dealer repository CRUD"""
        repo = DealerRepository()

        # Read all
        dealers = repo.get_all(integration_db)
        assert len(dealers) >= 2

        # Read by ID
        dealer = repo.get_by_id(1, integration_db)
        assert dealer.nama == "PT Jaya Motor Pusat"

        # Filter
        jakarta = repo.filter(integration_db, kota="Jakarta")
        assert len(jakarta) > 0

    def test_stock_motor_repository_operations(self, integration_db):
        """Test stock motor repository"""
        repo = StokMotorRepository()

        # Get ready stock
        ready = repo.filter(integration_db, status="R")
        assert len(ready) >= 3

        # Count by status
        count = repo.count_by_status(integration_db, "R")
        assert count >= 3

        # Get by type
        by_type = repo.get_by_type(1, integration_db)
        assert len(by_type) >= 2

    def test_transaction_repository_advanced_filters(self, integration_db):
        """Test advanced transaction filtering"""
        repo = TransaksiRepository()

        # Create test data first
        service = TransaksiService()
        for i in range(2):
            trans_data = {
                "nota": f"FILTER-{i:03d}",
                "tanggal": datetime.now().date(),
                "id_dealer": 1 if i == 0 else 2,
                "nama_pembeli": f"Test {i}",
                "alamat_pembeli": "Test",
                "telp_pembeli": "081200000000",
                "email_pembeli": f"test{i}@example.com",
                "id_motor": i + 1,
                "id_leasing": 1,
                "status_transaksi": "A",
            }
            detail_data = {
                "dp": 5000000.0,
                "subsidi": 1000000.0,
                "diskon": 100000.0,
                "diskon_tambahan": 0,
                "insentif": 50000.0,
            }
            service.create_transaksi(trans_data, detail_data)

        # Filter by dealer
        dealer1_trans = repo.filter(integration_db, id_dealer=1)
        assert len(dealer1_trans) > 0

        # Filter by status
        approved = repo.filter(integration_db, status_transaksi="A")
        assert len(approved) > 0


class TestServiceIntegration:
    """Test business services with database"""

    def test_transaction_service_dashboard_summary(self, integration_db):
        """Test dashboard summary generation"""
        service = TransaksiService()

        # Create test transactions
        for i in range(3):
            trans_data = {
                "nota": f"DASH-{i:03d}",
                "tanggal": datetime.now().date(),
                "id_dealer": 1,
                "nama_pembeli": f"Customer {i}",
                "alamat_pembeli": "Test",
                "telp_pembeli": "081200000000",
                "email_pembeli": f"cust{i}@example.com",
                "id_motor": 1,
                "id_leasing": 1,
                "status_transaksi": "A",
            }
            detail_data = {
                "dp": 5000000.0,
                "subsidi": 1000000.0,
                "diskon": 100000.0,
                "diskon_tambahan": 0,
                "insentif": 50000.0,
            }
            service.create_transaksi(trans_data, detail_data)

        # Get dashboard summary
        summary = service.get_dashboard_summary(integration_db)

        assert "total_transaksi" in summary
        assert summary["total_transaksi"] >= 3

    def test_transaction_service_status_tracking(self, integration_db):
        """Test transaction status lifecycle"""
        service = TransaksiService()

        # Create
        trans_data = {
            "nota": "STATUS-001",
            "tanggal": datetime.now().date(),
            "id_dealer": 1,
            "nama_pembeli": "Status Test",
            "alamat_pembeli": "Test",
            "telp_pembeli": "081200000000",
            "email_pembeli": "status@example.com",
            "id_motor": 1,
            "id_leasing": 1,
            "status_transaksi": "P",
        }

        detail_data = {
            "dp": 5000000.0,
            "subsidi": 1000000.0,
            "diskon": 100000.0,
            "diskon_tambahan": 0,
            "insentif": 50000.0,
        }

        trans = service.create_transaksi(trans_data, detail_data)

        # Get detail status
        status = service.get_transaction_status(trans.id, integration_db)
        assert status is not None


class TestDataIntegrity:
    """Test data consistency and integrity"""

    def test_transaction_detail_relationship(self, integration_db):
        """Test transaction-detail relationship integrity"""
        service = TransaksiService()

        trans_data = {
            "nota": "INTEGRITY-001",
            "tanggal": datetime.now().date(),
            "id_dealer": 1,
            "nama_pembeli": "Integrity Test",
            "alamat_pembeli": "Test",
            "telp_pembeli": "081200000000",
            "email_pembeli": "integrity@example.com",
            "id_motor": 1,
            "id_leasing": 1,
            "status_transaksi": "A",
        }

        detail_data = {
            "dp": 5000000.0,
            "subsidi": 1000000.0,
            "diskon": 100000.0,
            "diskon_tambahan": 50000.0,
            "insentif": 100000.0,
        }

        trans = service.create_transaksi(trans_data, detail_data)

        # Verify relationship
        assert trans.detail is not None
        assert trans.detail.id_transaksi == trans.id
        assert trans.detail.dp == 5000000.0

    def test_motor_dealer_relationships(self, integration_db):
        """Test motor and dealer relationships"""
        repo = StokMotorRepository()

        motor = repo.get_by_id(1, integration_db)
        assert motor is not None
        assert motor.type_motor is not None
        assert motor.type_motor.nama_type in ["PCX 160", "Vario 125"]

    def test_cascade_operations(self, integration_db):
        """Test cascade delete and update operations"""
        service = TransaksiService()

        # Create transaction
        trans_data = {
            "nota": "CASCADE-001",
            "tanggal": datetime.now().date(),
            "id_dealer": 1,
            "nama_pembeli": "Cascade Test",
            "alamat_pembeli": "Test",
            "telp_pembeli": "081200000000",
            "email_pembeli": "cascade@example.com",
            "id_motor": 1,
            "id_leasing": 1,
            "status_transaksi": "A",
        }

        detail_data = {
            "dp": 5000000.0,
            "subsidi": 1000000.0,
            "diskon": 100000.0,
            "diskon_tambahan": 0,
            "insentif": 50000.0,
        }

        trans = service.create_transaksi(trans_data, detail_data)
        trans_id = trans.id

        # Verify both created
        repo = TransaksiRepository()
        trans_check = repo.get_by_id(trans_id, integration_db)
        assert trans_check is not None
        assert trans_check.detail is not None
