"""
Repository Pattern - Data Access Layer
Provides generic CRUD operations and custom queries
"""

from abc import ABC, abstractmethod
from typing import List, Optional, Type, TypeVar, Generic, Dict, Any
from datetime import date, datetime

from sqlalchemy.orm import Session
from sqlalchemy import and_, or_, desc, asc

from database.connection import DatabaseManager

T = TypeVar('T')  # Generic type for model


class BaseRepository(ABC, Generic[T]):
    """
    Generic repository base class for all models.
    Implements common CRUD operations.

    Usage:
        class TransaksiRepository(BaseRepository[Transaksi]):
            def __init__(self, model_class=Transaksi):
                super().__init__(model_class)
    """

    def __init__(self, model_class: Type[T]):
        """
        Initialize repository with model class.

        Args:
            model_class: SQLAlchemy model class
        """
        self.model_class = model_class

    def get_session(self) -> Session:
        """Get database session"""
        return DatabaseManager.get_session()

    # =====================================================================
    # BASIC CRUD OPERATIONS
    # =====================================================================

    def get_all(self, skip: int = 0, limit: int = 100, order_by: str = None) -> List[T]:
        """
        Get all records with pagination.

        Args:
            skip: Number of records to skip
            limit: Maximum number of records to return
            order_by: Column name to order by (prefix with '-' for DESC)

        Returns:
            List of model instances

        Example:
            repo.get_all(skip=0, limit=50, order_by='-created_at')
        """
        session = self.get_session()
        # DO NOT close session - let Flask's app context handle it
        # This prevents lazy-load errors when accessing relationships after query
        query = session.query(self.model_class)

        # Apply ordering
        if order_by:
            if order_by.startswith('-'):
                column = getattr(self.model_class, order_by[1:])
                query = query.order_by(desc(column))
            else:
                column = getattr(self.model_class, order_by)
                query = query.order_by(asc(column))

        return query.offset(skip).limit(limit).all()

    def get_by_id(self, id: int) -> Optional[T]:
        """
        Get record by primary key.

        Args:
            id: Primary key value

        Returns:
            Model instance or None if not found
        """
        session = self.get_session()
        # DO NOT close session - let Flask's app context handle it
        # This prevents lazy-load errors when accessing relationships
        return session.query(self.model_class).filter(
            self.model_class.id == id
        ).first()

    def get_count(self) -> int:
        """
        Get total count of records.

        Returns:
            Total number of records
        """
        session = self.get_session()
        # DO NOT close session - let Flask's app context handle it
        return session.query(self.model_class).count()

    def create(self, data: Dict[str, Any]) -> T:
        """
        Create new record.

        Args:
            data: Dictionary of model attributes

        Returns:
            Created model instance

        Example:
            transaksi = repo.create({
                'nota': 'TRX001',
                'tanggal': date.today(),
                'dealer_id': 1,
                ...
            })
        """
        session = self.get_session()
        try:
            instance = self.model_class(**data)
            session.add(instance)
            session.commit()
            session.refresh(instance)
            return instance
        except Exception as e:
            session.rollback()
            raise e
        # DO NOT close session - let Flask's app context handle it

    def update(self, id: int, data: Dict[str, Any]) -> Optional[T]:
        """
        Update existing record.

        Args:
            id: Primary key of record to update
            data: Dictionary of attributes to update

        Returns:
            Updated model instance or None if not found

        Example:
            repo.update(1, {'status': 'A', 'nama': 'New Name'})
        """
        session = self.get_session()
        try:
            instance = session.query(self.model_class).filter(
                self.model_class.id == id
            ).first()

            if instance:
                for key, value in data.items():
                    if hasattr(instance, key):
                        setattr(instance, key, value)
                session.commit()
                session.refresh(instance)

            return instance
        except Exception as e:
            session.rollback()
            raise e
        # DO NOT close session - let Flask's app context handle it
        # This keeps returned instance attached for lazy-load operations

    def delete(self, id: int) -> bool:
        """
        Delete record by primary key.

        Args:
            id: Primary key of record to delete

        Returns:
            True if deleted, False if not found
        """
        session = self.get_session()
        try:
            instance = session.query(self.model_class).filter(
                self.model_class.id == id
            ).first()

            if instance:
                session.delete(instance)
                session.commit()
                return True

            return False
        except Exception as e:
            session.rollback()
            raise e
        # DO NOT close session - let Flask's app context handle it

    def delete_all(self) -> int:
        """
        Delete all records (DANGEROUS).

        Returns:
            Number of records deleted
        """
        session = self.get_session()
        try:
            count = session.query(self.model_class).delete()
            session.commit()
            return count
        except Exception as e:
            session.rollback()
            raise e
        # DO NOT close session - let Flask's app context handle it

    # =====================================================================
    # FILTER & SEARCH OPERATIONS
    # =====================================================================

    def filter(self, **kwargs) -> List[T]:
        """
        Filter records by multiple conditions (AND).

        Args:
            **kwargs: Column=value pairs for filtering

        Returns:
            List of matching records

        Example:
            repo.filter(status='A', dealer_id=1)
        """
        session = self.get_session()
        # DO NOT close session - let Flask's app context handle it
        query = session.query(self.model_class)

        for key, value in kwargs.items():
            if hasattr(self.model_class, key):
                query = query.filter(
                    getattr(self.model_class, key) == value
                )

        return query.all()

    def filter_or(self, **kwargs) -> List[T]:
        """
        Filter records by multiple conditions (OR).

        Args:
            **kwargs: Column=value pairs for filtering

        Returns:
            List of matching records

        Example:
            repo.filter_or(status='A', status='P')  # Status is A OR P
        """
        session = self.get_session()
        # DO NOT close session - let Flask's app context handle it
        query = session.query(self.model_class)
        conditions = []

        for key, value in kwargs.items():
            if hasattr(self.model_class, key):
                conditions.append(
                    getattr(self.model_class, key) == value
                )

        if conditions:
            query = query.filter(or_(*conditions))

        return query.all()

    def filter_like(self, column_name: str, value: str) -> List[T]:
        """
        Filter records using LIKE operator (case-insensitive).

        Args:
            column_name: Name of column to search
            value: Search value (% wildcards optional)

        Returns:
            List of matching records

        Example:
            repo.filter_like('nama', 'budi%')
        """
        session = self.get_session()
        # DO NOT close session - let Flask's app context handle it
        if not hasattr(self.model_class, column_name):
            return []

        column = getattr(self.model_class, column_name)
        return session.query(self.model_class).filter(
            column.ilike(f"%{value}%")
        ).all()

    def filter_between(self, column_name: str, start, end) -> List[T]:
        """
        Filter records by range (for dates, numbers, etc).

        Args:
            column_name: Name of column to filter
            start: Start of range
            end: End of range

        Returns:
            List of matching records

        Example:
            repo.filter_between('tanggal', date(2024, 1, 1), date(2024, 12, 31))
        """
        session = self.get_session()
        # DO NOT close session - let Flask's app context handle it
        if not hasattr(self.model_class, column_name):
            return []

        column = getattr(self.model_class, column_name)
        return session.query(self.model_class).filter(
            column.between(start, end)
        ).all()

    def filter_in(self, column_name: str, values: list) -> List[T]:
        """
        Filter records where column value is in list.

        Args:
            column_name: Name of column to filter
            values: List of values to match

        Returns:
            List of matching records

        Example:
            repo.filter_in('status', ['A', 'P', 'L'])
        """
        session = self.get_session()
        # DO NOT close session - let Flask's app context handle it
        if not hasattr(self.model_class, column_name):
            return []

        column = getattr(self.model_class, column_name)
        return session.query(self.model_class).filter(
            column.in_(values)
        ).all()

    def filter_null(self, column_name: str, is_null: bool = True) -> List[T]:
        """
        Filter records where column is NULL or NOT NULL.

        Args:
            column_name: Name of column to check
            is_null: True for NULL, False for NOT NULL

        Returns:
            List of matching records

        Example:
            repo.filter_null('broker_id', is_null=True)  # No broker
        """
        session = self.get_session()
        # DO NOT close session - let Flask's app context handle it
        if not hasattr(self.model_class, column_name):
            return []

        column = getattr(self.model_class, column_name)
        if is_null:
            return session.query(self.model_class).filter(
                column.is_(None)
            ).all()
        else:
            return session.query(self.model_class).filter(
                column.isnot(None)
            ).all()

    # =====================================================================
    # EXISTENCE CHECKS
    # =====================================================================

    def exists(self, **kwargs) -> bool:
        """
        Check if record exists.

        Args:
            **kwargs: Column=value pairs for checking

        Returns:
            True if record exists, False otherwise

        Example:
            if repo.exists(nota='TRX001'):
                print("Transaction already exists")
        """
        session = self.get_session()
        # DO NOT close session - let Flask's app context handle it
        query = session.query(self.model_class)

        for key, value in kwargs.items():
            if hasattr(self.model_class, key):
                query = query.filter(
                    getattr(self.model_class, key) == value
                )

        return query.first() is not None

    def exists_by_id(self, id: int) -> bool:
        """
        Check if record exists by ID.

        Args:
            id: Primary key value

        Returns:
            True if exists, False otherwise
        """
        return self.get_by_id(id) is not None

    # =====================================================================
    # BULK OPERATIONS
    # =====================================================================

    def create_bulk(self, data_list: List[Dict[str, Any]]) -> List[T]:
        """
        Create multiple records at once.

        Args:
            data_list: List of dictionaries with model attributes

        Returns:
            List of created instances

        Example:
            repos.create_bulk([
                {'nota': 'TRX001', 'tanggal': date.today(), ...},
                {'nota': 'TRX002', 'tanggal': date.today(), ...},
            ])
        """
        session = self.get_session()
        try:
            instances = []
            for data in data_list:
                instance = self.model_class(**data)
                session.add(instance)
                instances.append(instance)

            session.commit()

            # Refresh all instances
            for instance in instances:
                session.refresh(instance)

            return instances
        except Exception as e:
            session.rollback()
            raise e
        # DO NOT close session - let Flask's app context handle it

    def update_bulk(self, updates: List[Dict[str, Any]]) -> List[T]:
        """
        Update multiple records.

        Args:
            updates: List of dicts with 'id' and other fields to update

        Returns:
            List of updated instances

        Example:
            repo.update_bulk([
                {'id': 1, 'status': 'A'},
                {'id': 2, 'status': 'L'},
            ])
        """
        session = self.get_session()
        try:
            instances = []

            for update_dict in updates:
                id_val = update_dict.pop('id')
                instance = session.query(self.model_class).filter(
                    self.model_class.id == id_val
                ).first()

                if instance:
                    for key, value in update_dict.items():
                        if hasattr(instance, key):
                            setattr(instance, key, value)
                    instances.append(instance)

            session.commit()
            return instances
        except Exception as e:
            session.rollback()
            raise e
        # DO NOT close session - let Flask's app context handle it

    # =====================================================================
    # EXPORT/IMPORT
    # =====================================================================

    def to_dict_list(self, instances: List[T]) -> List[Dict[str, Any]]:
        """
        Convert model instances to list of dictionaries.

        Args:
            instances: List of model instances

        Returns:
            List of dictionaries
        """
        result = []
        for instance in instances:
            data = {}
            for column in instance.__table__.columns:
                data[column.name] = getattr(instance, column.name)
            result.append(data)
        return result

    def to_dict(self, instance: T) -> Dict[str, Any]:
        """
        Convert model instance to dictionary.

        Args:
            instance: Model instance

        Returns:
            Dictionary representation
        """
        if not instance:
            return {}

        data = {}
        for column in instance.__table__.columns:
            value = getattr(instance, column.name)
            # Convert datetime to string for JSON serialization
            if isinstance(value, (datetime, date)):
                value = value.isoformat()
            data[column.name] = value
        return data

    # =====================================================================
    # HELPER METHODS
    # =====================================================================

    def attach_to_session(self, instance: T, session: Session = None):
        """Attach instance to session"""
        if session is None:
            session = self.get_session()
        if instance not in session:
            session.merge(instance)

    def detach_from_session(self, instance: T, session: Session = None):
        """Detach instance from session"""
        if session is None:
            session = self.get_session()
        if instance in session:
            session.expunge(instance)

    def refresh(self, instance: T):
        """Refresh instance from database"""
        session = self.get_session()
        # DO NOT close session - let Flask's app context handle it
        session.refresh(instance)
