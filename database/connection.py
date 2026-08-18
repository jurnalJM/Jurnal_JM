"""
Database Connection Management
Handles SQLite database connection, session management, and transactions
"""

import os
from contextlib import contextmanager
from typing import Generator

from sqlalchemy import create_engine, event, text
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.pool import StaticPool

from config import DATABASE_URL, DB_ECHO, DB_POOL_SIZE, DB_MAX_OVERFLOW, DB_ENABLE_FK, DB_SSL_REQUIRED


class DatabaseManager:
    """Singleton database manager for application-wide database access"""

    _instance = None
    _engine = None
    _session_factory = None

    def __new__(cls):
        """Ensure only one instance of DatabaseManager exists"""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def initialize(cls, database_url: str = None, echo: bool = None):
        """
        Initialize database connection.

        Args:
            database_url: SQLAlchemy database URL (if None, uses config.DATABASE_URL)
            echo: Whether to log SQL queries (if None, uses config.DB_ECHO)
        """
        if database_url is None:
            database_url = DATABASE_URL

        if echo is None:
            echo = DB_ECHO

        # SQLite specific configuration
        if database_url.startswith("sqlite"):
            # Use StaticPool to avoid threading issues with SQLite
            cls._engine = create_engine(
                database_url,
                echo=echo,
                connect_args={"check_same_thread": False},
                poolclass=StaticPool,
            )
        else:
            connect_args = {}
            if DB_SSL_REQUIRED:
                import certifi

                connect_args = {
                    "ssl_ca": certifi.where(),
                    "ssl_verify_cert": True,
                    "ssl_verify_identity": True,
                }

            cls._engine = create_engine(
                database_url,
                echo=echo,
                pool_size=DB_POOL_SIZE,
                max_overflow=DB_MAX_OVERFLOW,
                pool_recycle=280,
                connect_args=connect_args,
            )

        # Enable foreign keys in SQLite
        if DB_ENABLE_FK and database_url.startswith("sqlite"):

            @event.listens_for(cls._engine, "connect")
            def set_sqlite_pragma(dbapi_conn, connection_record):
                cursor = dbapi_conn.cursor()
                cursor.execute("PRAGMA foreign_keys=ON")
                cursor.close()

        # Create session factory
        cls._session_factory = sessionmaker(bind=cls._engine)

    @classmethod
    def get_engine(cls):
        """Get SQLAlchemy engine"""
        if cls._engine is None:
            cls.initialize()
        return cls._engine

    @classmethod
    def get_session(cls) -> Session:
        """
        Get a new database session.

        Returns:
            SQLAlchemy Session object
        """
        if cls._session_factory is None:
            cls.initialize()
        return cls._session_factory()

    @classmethod
    @contextmanager
    def session_context(cls) -> Generator[Session, None, None]:
        """
        Context manager for database session.
        Automatically commits on success, rolls back on exception.

        Usage:
            with DatabaseManager.session_context() as session:
                # do something with session
                session.query(Model).all()
        """
        session = cls.get_session()
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    @classmethod
    @contextmanager
    def transaction(cls) -> Generator[Session, None, None]:
        """
        Context manager for database transaction.
        Alias for session_context()
        """
        with cls.session_context() as session:
            yield session

    @classmethod
    def create_all_tables(cls):
        """Create all database tables"""
        from database.models import Base

        Base.metadata.create_all(cls.get_engine())

    @classmethod
    def drop_all_tables(cls):
        """Drop all database tables (DANGEROUS - use only for testing)"""
        from database.models import Base

        Base.metadata.drop_all(cls.get_engine())

    @classmethod
    def execute_raw_sql(cls, sql: str, params: dict = None):
        """
        Execute raw SQL query.

        Args:
            sql: SQL query string
            params: Query parameters (for prepared statements)

        Returns:
            Query result
        """
        with cls.session_context() as session:
            result = session.execute(text(sql), params or {})
            session.commit()
            return result

    @classmethod
    def close_all_connections(cls):
        """Close all database connections"""
        if cls._engine is not None:
            cls._engine.dispose()


# Convenience function for getting session
def get_session() -> Session:
    """
    Get a new database session.

    Returns:
        SQLAlchemy Session object

    Usage:
        session = get_session()
        try:
            # do something
            pass
        finally:
            session.close()
    """
    return DatabaseManager.get_session()


# Convenience context manager
@contextmanager
def session_context() -> Generator[Session, None, None]:
    """
    Context manager for database session with auto-commit/rollback.

    Usage:
        with session_context() as session:
            session.query(Model).all()
    """
    with DatabaseManager.session_context() as session:
        yield session


# Initialize database on module import
if __name__ != "__main__":
    # Only auto-initialize if this module is imported
    # When run directly, user must call initialize() manually
    try:
        DatabaseManager.initialize()
    except Exception as e:
        print(f"Warning: Could not auto-initialize database: {e}")
