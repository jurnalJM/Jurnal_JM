"""
Pytest Configuration and Shared Fixtures
"""

import pytest
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from database.connection import DatabaseManager
from database.models import Base


@pytest.fixture(scope="session")
def test_database_url():
    """In-memory SQLite database URL for testing"""
    return "sqlite:///:memory:"


@pytest.fixture(scope="function")
def db_session(test_database_url):
    """
    Create a test database session.

    Creates fresh database for each test, then cleans up after.
    """
    # Initialize with in-memory database
    DatabaseManager.initialize(test_database_url)

    # Create all tables
    Base.metadata.create_all(DatabaseManager.get_engine())

    yield DatabaseManager.get_session()

    # Cleanup
    Base.metadata.drop_all(DatabaseManager.get_engine())
    DatabaseManager.close_all_connections()


@pytest.fixture(scope="function")
def db_with_seed(test_database_url):
    """
    Create a test database with seed data.
    """
    # Initialize with in-memory database
    DatabaseManager.initialize(test_database_url)

    # Create all tables
    Base.metadata.create_all(DatabaseManager.get_engine())

    # Seed initial data
    from database.schema import seed_master_data
    with DatabaseManager.session_context() as session:
        seed_master_data()

    yield DatabaseManager.get_session()

    # Cleanup
    Base.metadata.drop_all(DatabaseManager.get_engine())
    DatabaseManager.close_all_connections()


@pytest.fixture(autouse=True)
def reset_db():
    """Auto-reset database between tests"""
    yield

    # Close all connections after each test
    try:
        DatabaseManager.close_all_connections()
    except:
        pass
