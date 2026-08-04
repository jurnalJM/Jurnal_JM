#!/usr/bin/env python
"""
Clear Database Script
Deletes database.db and reinitializes with seed data only.
Usage: python clear_data.py
"""

import os
import sys
from pathlib import Path

def clear_database():
    """Delete database and reinitialize"""
    db_path = Path("database.db")

    # Delete if exists
    if db_path.exists():
        print(f"Deleting {db_path}...")
        db_path.unlink()
        print("✓ Database deleted")
    else:
        print("Database file not found, creating new...")

    # Reinitialize
    print("\nReinitializing database...")
    try:
        from database.connection import DatabaseManager
        from database.schema import initialize_database

        initialize_database()
        print("\n✓ Database reset complete!")
        print("✓ Master data (Dealer, Leasing, Broker, Types) seeded")
        print("✓ Ready for testing")

    except Exception as e:
        print(f"✗ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Confirm
    response = input("\n⚠️  This will DELETE all data. Continue? (yes/no): ").strip().lower()
    if response != 'yes':
        print("Cancelled.")
        sys.exit(0)

    clear_database()
