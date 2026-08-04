#!/usr/bin/env python
"""
Backup Database Script
Creates a timestamped backup of database.db
"""

import shutil
from pathlib import Path
from datetime import datetime

def backup_database():
    """Create timestamped backup of database"""
    db_path = Path("database.db")
    backup_dir = Path("backups")

    if not db_path.exists():
        print("✗ Database file not found")
        return False

    # Create backups directory if not exists
    backup_dir.mkdir(exist_ok=True)

    # Create backup with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = backup_dir / f"database_{timestamp}.db"

    try:
        shutil.copy2(db_path, backup_path)
        print(f"✓ Backup created: {backup_path}")
        return True
    except Exception as e:
        print(f"✗ Backup failed: {e}")
        return False

if __name__ == "__main__":
    backup_database()
