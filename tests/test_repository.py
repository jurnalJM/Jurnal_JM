"""
Unit Tests for Repository Classes
Tests CRUD operations and custom queries
"""

import pytest
from datetime import date, datetime, timedelta
from pathlib import Path
import os

from database.connection import DatabaseManager
from database.schema import initialize_database, reset_database
from database.models import Base
from database.repositories import (
    DealerRepository,
    TransaksiRepository,
    TypeMotorRepository,
    StokMotorRepository,
    LeasingRepository,
    BrokerRepository,
)


# =====================================================================
# FIXTURES
# =====================================================================

@pytest.fixture(scope="module")
def test_db():
    """Setup test database"""
    # Use in-memory SQLite for testing
    test_db_url = "sqlite:///:memory:"

    # Initialize database
    DatabaseManager.initialize(test_db_url)
    Base.metadata.create_all(DatabaseManager.get_engine())

    # Seed test data
    from database.schema import seed_master_data

    with DatabaseManager.session_context() as session:
        seed_master_data()

    yield test_db_url

    # Cleanup
    DatabaseManager.drop_all_tables()
    DatabaseManager.close_all_connections()


# =====================================================================
# DEALER REPOSITORY TESTS
# =====================================================================

class TestDealerRepository:
    """Test cases for DealerRepository"""

    def test_get_all(self, test_db):
        """Test getting all dealers"""
        repo = DealerRepository()
        dealers = repo.get_all()

        assert len(dealers) >= 3
        assert dealers[0].nama in ["Jaya Motor Pusat", "Jaya Motor BSD", "Jaya Motor Bekasi"]

    def test_get_by_id(self, test_db):
        """Test getting dealer by ID"""
        repo = DealerRepository()
        dealer = repo.get_by_id(1)

        assert dealer is not None
        assert dealer.id == 1
        assert dealer.nama == "Jaya Motor Pusat"

    def test_get_by_name(self, test_db):
        """Test getting dealer by name"""
        repo = DealerRepository()
        dealer = repo.get_by_name("Jaya Motor BSD")

        assert dealer is not None
        assert dealer.nama == "Jaya Motor BSD"
        assert dealer.kota == "Tangerang Selatan"

    def test_get_active(self, test_db):
        """Test getting active dealers"""
        repo = DealerRepository()
        dealers = repo.get_active()

        assert len(dealers) >= 3
        assert all(d.status == "A" for d in dealers)

    def test_create_dealer(self, test_db):
        """Test creating new dealer"""
        repo = DealerRepository()
        data = {
            "nama": "Jaya Motor Bogor",
            "alamat": "Jl. Raya Bogor",
            "kota": "Bogor",
            "telp": "0251-123456",
            "status": "A",
        }

        dealer = repo.create(data)

        assert dealer.id is not None
        assert dealer.nama == "Jaya Motor Bogor"
        assert dealer.kota == "Bogor"

    def test_update_dealer(self, test_db):
        """Test updating dealer"""
        repo = DealerRepository()
        dealer = repo.update(1, {"status": "I"})

        assert dealer is not None
        assert dealer.status == "I"

    def test_delete_dealer(self, test_db):
        """Test deleting dealer"""
        repo = DealerRepository()
        # Create a dealer to delete
        new_dealer = repo.create({
            "nama": "Temporary Dealer",
            "status": "A",
        })
        dealer_id = new_dealer.id

        # Delete it
        result = repo.delete(dealer_id)

        assert result is True
        assert repo.get_by_id(dealer_id) is None

    def test_search_by_city(self, test_db):
        """Test searching dealers by city"""
        repo = DealerRepository()
        dealers = repo.search_by_city("Jakarta")

        assert len(dealers) >= 1


# =====================================================================
# TYPE MOTOR REPOSITORY TESTS
# =====================================================================

class TestTypeMotorRepository:
    """Test cases for TypeMotorRepository"""

    def test_get_all_types(self, test_db):
        """Test getting all motor types"""
        repo = TypeMotorRepository()
        types = repo.get_all()

        assert len(types) >= 4

    def test_get_by_kode(self, test_db):
        """Test getting motor type by code"""
        repo = TypeMotorRepository()
        motor_type = repo.get_by_kode("H-CB150")

        assert motor_type is not None
        assert motor_type.nama_type == "Honda CB 150"
        assert motor_type.merek == "Honda"

    def test_get_active_types(self, test_db):
        """Test getting active motor types"""
        repo = TypeMotorRepository()
        types = repo.get_active()

        assert len(types) >= 4
        assert all(t.status == "A" for t in types)

    def test_get_by_merek(self, test_db):
        """Test getting motor types by brand"""
        repo = TypeMotorRepository()
        hondas = repo.get_by_merek("Honda")

        assert len(hondas) >= 1
        assert all(t.merek == "Honda" for t in hondas)

    def test_search_by_name(self, test_db):
        """Test searching motor types by name"""
        repo = TypeMotorRepository()
        results = repo.search_by_name("Honda")

        assert len(results) >= 1

    def test_get_by_cc_range(self, test_db):
        """Test getting motor types by engine size"""
        repo = TypeMotorRepository()
        results = repo.get_by_cc_range(100, 150)

        assert len(results) >= 1


# =====================================================================
# LEASING REPOSITORY TESTS
# =====================================================================

class TestLeasingRepository:
    """Test cases for LeasingRepository"""

    def test_get_all_leasing(self, test_db):
        """Test getting all leasing companies"""
        repo = LeasingRepository()
        leasings = repo.get_all()

        assert len(leasings) >= 4

    def test_get_by_kode(self, test_db):
        """Test getting leasing by code"""
        repo = LeasingRepository()
        leasing = repo.get_by_kode("BCA")

        assert leasing is not None
        assert leasing.nama == "BCA Finance"

    def test_get_active_leasing(self, test_db):
        """Test getting active leasing companies"""
        repo = LeasingRepository()
        leasings = repo.get_active()

        assert len(leasings) >= 4
        assert all(l.status == "A" for l in leasings)


# =====================================================================
# BROKER REPOSITORY TESTS
# =====================================================================

class TestBrokerRepository:
    """Test cases for BrokerRepository"""

    def test_get_all_brokers(self, test_db):
        """Test getting all brokers"""
        repo = BrokerRepository()
        brokers = repo.get_all()

        assert len(brokers) >= 3

    def test_get_active_brokers(self, test_db):
        """Test getting active brokers"""
        repo = BrokerRepository()
        brokers = repo.get_active()

        assert len(brokers) >= 3
        assert all(b.status == "A" for b in brokers)


# =====================================================================
# STOK MOTOR REPOSITORY TESTS
# =====================================================================

class TestStokMotorRepository:
    """Test cases for StokMotorRepository"""

    def test_create_stok(self, test_db):
        """Test creating vehicle in stock"""
        repo = StokMotorRepository()
        data = {
            "no_mesin": "MKA12345678",
            "no_rangka": "MKR12345678",
            "type_id": 1,
            "warna": "Merah",
            "tahun_produksi": 2024,
            "tgl_datang": date.today(),
            "dealer_id": 1,
            "status": "R",
        }

        stok = repo.create(data)

        assert stok.id is not None
        assert stok.no_mesin == "MKA12345678"
        assert stok.status == "R"

    def test_get_by_no_mesin(self, test_db):
        """Test getting vehicle by engine number"""
        repo = StokMotorRepository()

        # Create one first
        stok = repo.create({
            "no_mesin": "TEST123456",
            "no_rangka": "TEST123456R",
            "type_id": 1,
            "tgl_datang": date.today(),
            "status": "R",
        })

        # Then retrieve
        found = repo.get_by_no_mesin("TEST123456")
        assert found is not None
        assert found.id == stok.id

    def test_get_ready(self, test_db):
        """Test getting ready vehicles"""
        repo = StokMotorRepository()

        # Create some ready vehicles
        for i in range(2):
            repo.create({
                "no_mesin": f"READY{i}",
                "no_rangka": f"READY{i}R",
                "type_id": 1,
                "tgl_datang": date.today(),
                "status": "R",
            })

        ready = repo.get_ready()
        assert len(ready) >= 2

    def test_count_by_status(self, test_db):
        """Test counting vehicles by status"""
        repo = StokMotorRepository()
        counts = repo.count_by_status()

        assert isinstance(counts, dict)
        assert "R" in counts  # Ready
        assert "S" in counts  # Sold
        assert counts["R"] >= 2  # We created some above


# =====================================================================
# TRANSAKSI REPOSITORY TESTS
# =====================================================================

class TestTransaksiRepository:
    """Test cases for TransaksiRepository"""

    def test_create_transaksi(self, test_db):
        """Test creating transaction"""
        repo = TransaksiRepository()
        data = {
            "nota": "TRX001",
            "tanggal": date.today(),
            "dealer_id": 1,
            "nama_pembeli": "Budi Santoso",
            "alamat_pembeli": "Jl. Merdeka 123",
            "telp_pembeli": "0812345678",
            "motor_id": 1,
        }

        transaksi = repo.create(data)

        assert transaksi.id is not None
        assert transaksi.nota == "TRX001"
        assert transaksi.status_transaksi == "P"  # Default status

    def test_get_by_nota(self, test_db):
        """Test getting transaction by nota"""
        repo = TransaksiRepository()

        # Create one
        trx = repo.create({
            "nota": "TRX002",
            "tanggal": date.today(),
            "dealer_id": 1,
            "nama_pembeli": "Siti Nurhaliza",
            "motor_id": 1,
        })

        # Retrieve
        found = repo.get_by_nota("TRX002")
        assert found is not None
        assert found.id == trx.id

    def test_nota_uniqueness(self, test_db):
        """Test that nota must be unique"""
        repo = TransaksiRepository()

        # Create first
        repo.create({
            "nota": "TRX003",
            "tanggal": date.today(),
            "dealer_id": 1,
            "nama_pembeli": "Test User",
            "motor_id": 1,
        })

        # Try to create another with same nota
        with pytest.raises(Exception):  # Should raise integrity error
            repo.create({
                "nota": "TRX003",
                "tanggal": date.today(),
                "dealer_id": 1,
                "nama_pembeli": "Another User",
                "motor_id": 2,
            })

    def test_search_by_customer(self, test_db):
        """Test searching transaction by customer"""
        repo = TransaksiRepository()

        # Create
        repo.create({
            "nota": "TRX004",
            "tanggal": date.today(),
            "dealer_id": 1,
            "nama_pembeli": "Ahmad Wijaya",
            "telp_pembeli": "0899999999",
            "motor_id": 1,
        })

        # Search by name
        results = repo.search_by_customer("Ahmad")
        assert len(results) >= 1
        assert any(r.nama_pembeli == "Ahmad Wijaya" for r in results)

        # Search by phone
        results = repo.search_by_customer("0899999999")
        assert len(results) >= 1

    def test_get_by_date_range(self, test_db):
        """Test getting transactions by date range"""
        repo = TransaksiRepository()

        # Create
        repo.create({
            "nota": "TRX005",
            "tanggal": date.today(),
            "dealer_id": 1,
            "nama_pembeli": "Test User",
            "motor_id": 1,
        })

        # Query range
        start = date.today() - timedelta(days=1)
        end = date.today() + timedelta(days=1)
        results = repo.get_by_date_range(start, end)

        assert len(results) >= 1

    def test_get_summary(self, test_db):
        """Test getting transaction summary"""
        repo = TransaksiRepository()

        start = date.today() - timedelta(days=1)
        end = date.today() + timedelta(days=1)
        summary = repo.get_summary(start, end)

        assert "total_transaksi" in summary
        assert "total_dp" in summary
        assert summary["total_transaksi"] >= 0


# =====================================================================
# FILTER OPERATIONS TESTS
# =====================================================================

class TestFilterOperations:
    """Test filter and search operations"""

    def test_filter_exact_match(self, test_db):
        """Test exact match filter"""
        repo = DealerRepository()
        dealers = repo.filter(status="A")

        assert len(dealers) >= 3
        assert all(d.status == "A" for d in dealers)

    def test_filter_like(self, test_db):
        """Test LIKE filter"""
        repo = DealerRepository()
        dealers = repo.filter_like("nama", "Jaya%")

        assert len(dealers) >= 3

    def test_filter_in(self, test_db):
        """Test IN filter"""
        repo = TypeMotorRepository()
        types = repo.filter_in("merek", ["Honda", "Yamaha"])

        assert len(types) >= 2

    def test_filter_between(self, test_db):
        """Test BETWEEN filter"""
        repo = TypeMotorRepository()
        types = repo.filter_between("cc", 100, 150)

        assert len(types) >= 1

    def test_exists(self, test_db):
        """Test exists check"""
        repo = DealerRepository()

        exists = repo.exists(nama="Jaya Motor Pusat")
        assert exists is True

        not_exists = repo.exists(nama="NonExistent")
        assert not_exists is False


# =====================================================================
# BULK OPERATIONS TESTS
# =====================================================================

class TestBulkOperations:
    """Test bulk create/update operations"""

    def test_create_bulk(self, test_db):
        """Test bulk create"""
        repo = TransaksiRepository()
        data = [
            {
                "nota": f"BULK{i}",
                "tanggal": date.today(),
                "dealer_id": 1,
                "nama_pembeli": f"Customer {i}",
                "motor_id": 1,
            }
            for i in range(3)
        ]

        transactions = repo.create_bulk(data)

        assert len(transactions) == 3
        for t in transactions:
            assert t.id is not None


# =====================================================================
# EXPORT/IMPORT TESTS
# =====================================================================

class TestExportImport:
    """Test export to dict operations"""

    def test_to_dict(self, test_db):
        """Test converting model to dict"""
        repo = DealerRepository()
        dealer = repo.get_by_id(1)

        dealer_dict = repo.to_dict(dealer)

        assert isinstance(dealer_dict, dict)
        assert "id" in dealer_dict
        assert "nama" in dealer_dict
        assert dealer_dict["id"] == 1

    def test_to_dict_list(self, test_db):
        """Test converting models to dict list"""
        repo = DealerRepository()
        dealers = repo.get_all(limit=3)

        dealer_list = repo.to_dict_list(dealers)

        assert isinstance(dealer_list, list)
        assert len(dealer_list) == len(dealers)
        assert all("id" in d for d in dealer_list)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
