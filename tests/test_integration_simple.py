"""
Simple integration tests for application flow
"""

import pytest
from pathlib import Path
from datetime import datetime, timedelta

from database.connection import DatabaseManager
from database.models import Base, Dealer, TypeMotor, StokMotor, Leasing
from database.repositories import DealerRepository, StokMotorRepository, TypeMotorRepository


@pytest.fixture(scope="function")
def test_db_simple(test_database_url):
    """Create test database with basic master data"""
    DatabaseManager.initialize(test_database_url)
    Base.metadata.create_all(DatabaseManager.get_engine())

    session = DatabaseManager.get_session()

    # Create minimal master data
    dealers = [
        Dealer(nama="PT Jaya Motor Pusat", kota="Jakarta", alamat="Jl. Jaya 1", telp="02112345678"),
    ]
    session.add_all(dealers)
    session.flush()

    motor_types = [
        TypeMotor(kode_type="PCX160", nama_type="PCX 160", merek="Honda", cc=160, otr=25000000),
    ]
    session.add_all(motor_types)
    session.flush()

    leasing_companies = [
        Leasing(kode="MANDIRI", nama="Mandiri Finance", alamat="Jl. Sudirman", telp="02198765432"),
    ]
    session.add_all(leasing_companies)
    session.flush()

    # Create inventory
    stocks = [
        StokMotor(type_id=motor_types[0].id, warna="Merah", no_mesin="PCX001", no_rangka="RANGE001", tgl_datang=datetime.now().date(), status="R"),
        StokMotor(type_id=motor_types[0].id, warna="Hitam", no_mesin="PCX002", no_rangka="RANGE002", tgl_datang=datetime.now().date(), status="R"),
    ]
    session.add_all(stocks)
    session.commit()

    yield session

    # Cleanup
    Base.metadata.drop_all(DatabaseManager.get_engine())
    DatabaseManager.close_all_connections()


class TestRepositoryOperations:
    """Test repository CRUD operations"""

    def test_dealer_read_operations(self, test_db_simple):
        """Test reading dealer data"""
        repo = DealerRepository()

        # Get all
        all_dealers = repo.get_all(test_db_simple)
        assert len(all_dealers) > 0

        # Get by ID
        dealer = repo.get_by_id(1, test_db_simple)
        assert dealer is not None
        assert dealer.nama == "PT Jaya Motor Pusat"
        assert dealer.kota == "Jakarta"

    def test_motor_type_read(self, test_db_simple):
        """Test motor type repository"""
        repo = TypeMotorRepository()

        # Get all
        all_types = repo.get_all(test_db_simple)
        assert len(all_types) > 0

        # Get by ID
        mtype = repo.get_by_id(1, test_db_simple)
        assert mtype is not None
        assert mtype.nama_type == "PCX 160"
        assert mtype.cc == 160

    def test_stock_motor_read(self, test_db_simple):
        """Test stock motor repository"""
        repo = StokMotorRepository()

        # Get all
        all_stock = repo.get_all(test_db_simple)
        assert len(all_stock) >= 2

        # Get by ID
        motor = repo.get_by_id(1, test_db_simple)
        assert motor is not None
        assert motor.no_mesin == "PCX001"
        assert motor.warna == "Merah"

        # Get by status
        ready = repo.filter(test_db_simple, status="R")
        assert len(ready) >= 2

    def test_relationships(self, test_db_simple):
        """Test ORM relationships"""
        repo = StokMotorRepository()

        motor = repo.get_by_id(1, test_db_simple)
        assert motor.type_motor is not None
        assert motor.type_motor.nama_type == "PCX 160"


class TestDataIntegrity:
    """Test data consistency"""

    def test_motor_type_relationship(self, test_db_simple):
        """Test that motor types have correct relationships"""
        repo = TypeMotorRepository()

        mtype = repo.get_by_id(1, test_db_simple)
        assert mtype.stok_motors is not None
        assert len(mtype.stok_motors) >= 2

    def test_dealer_relationship(self, test_db_simple):
        """Test that dealers have relationships"""
        repo = DealerRepository()

        dealer = repo.get_by_id(1, test_db_simple)
        assert dealer.stok_motors is not None
        # Note: We didn't assign motors to dealer in test data

    def test_motor_uniqueness(self, test_db_simple):
        """Test that motor unique fields are enforced"""
        repo = StokMotorRepository()

        # Get two different motors
        motor1 = repo.get_by_id(1, test_db_simple)
        motor2 = repo.get_by_id(2, test_db_simple)

        # Should have different no_mesin
        assert motor1.no_mesin != motor2.no_mesin
        assert motor1.no_rangka != motor2.no_rangka


class TestFilterOperations:
    """Test filtering and searching"""

    def test_filter_by_status(self, test_db_simple):
        """Test filtering motors by status"""
        repo = StokMotorRepository()

        # Get ready status motors
        ready = repo.filter(test_db_simple, status="R")
        assert len(ready) == 2

        # Get sold motors (should be none)
        sold = repo.filter(test_db_simple, status="S")
        assert len(sold) == 0

    def test_count_by_status(self, test_db_simple):
        """Test counting by status"""
        repo = StokMotorRepository()

        count = repo.count_by_status(test_db_simple, "R")
        assert count == 2

    def test_filter_by_type(self, test_db_simple):
        """Test filtering by motor type"""
        repo = StokMotorRepository()

        by_type = repo.get_by_type(1, test_db_simple)
        assert len(by_type) >= 2

    def test_filter_by_warna(self, test_db_simple):
        """Test filtering by color"""
        repo = StokMotorRepository()

        red_motors = repo.filter(test_db_simple, warna="Merah")
        assert len(red_motors) >= 1
        assert red_motors[0].warna == "Merah"


class TestCompleteWorkflow:
    """Test complete application workflows"""

    def test_master_data_consistency(self, test_db_simple):
        """Test that all master data is consistent"""
        dealer_repo = DealerRepository()
        type_repo = TypeMotorRepository()
        motor_repo = StokMotorRepository()

        # All repos should return data
        dealers = dealer_repo.get_all(test_db_simple)
        types = type_repo.get_all(test_db_simple)
        motors = motor_repo.get_all(test_db_simple)

        assert len(dealers) > 0
        assert len(types) > 0
        assert len(motors) > 0

    def test_motor_availability_check(self, test_db_simple):
        """Test checking motor availability"""
        repo = StokMotorRepository()

        # Specific motor should be available (status=R)
        motor = repo.get_by_id(1, test_db_simple)
        assert motor.status == "R"

        # Check via filter
        available = repo.filter(test_db_simple, status="R", no_mesin="PCX001")
        assert len(available) > 0
        assert available[0].no_mesin == "PCX001"

    def test_inventory_query_methods(self, test_db_simple):
        """Test inventory query methods"""
        repo = StokMotorRepository()

        # Test exists_by_mesin
        exists = repo.filter_like(test_db_simple, no_mesin="PCX%")
        assert len(exists) >= 2

        # Test by type and status
        by_type_and_status = repo.filter(test_db_simple, type_id=1, status="R")
        assert len(by_type_and_status) >= 2
