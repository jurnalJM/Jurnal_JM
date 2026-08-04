#!/usr/bin/env python
"""
Undo Import Script
Restore database from most recent backup
"""

import shutil
import sys
from pathlib import Path
from datetime import datetime

def list_backups():
    """List all available backups"""
    backup_dir = Path("backups")

    if not backup_dir.exists():
        print("✗ No backups found")
        return []

    backups = sorted(backup_dir.glob("database_*.db"), reverse=True)

    if not backups:
        print("✗ No backups found in backups directory")
        return []

    print("\nAvailable backups:")
    print("-" * 60)
    for i, backup in enumerate(backups[:10], 1):  # Show last 10
        size_mb = backup.stat().st_size / (1024 * 1024)
        mod_time = datetime.fromtimestamp(backup.stat().st_mtime)
        print(f"{i}. {backup.name} ({size_mb:.1f} MB) - {mod_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 60)

    return backups

def restore_from_backup(backup_path):
    """Restore database from backup"""
    db_path = Path("database.db")

    if not backup_path.exists():
        print(f"✗ Backup file not found: {backup_path}")
        return False

    # Backup current database before restore
    if db_path.exists():
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        current_backup = Path("backups") / f"database_current_{timestamp}.db"
        current_backup.parent.mkdir(exist_ok=True)
        shutil.copy2(db_path, current_backup)
        print(f"✓ Current database backed up to: {current_backup}")

    # Restore from backup
    try:
        shutil.copy2(backup_path, db_path)
        print(f"✓ Database restored from: {backup_path}")
        print("✓ All imported data has been removed")
        return True
    except Exception as e:
        print(f"✗ Restore failed: {e}")
        return False

def main():
    """Interactive restore"""
    print("\n" + "=" * 60)
    print("     JayaMotor - Undo Import")
    print("=" * 60)

    backups = list_backups()
    if not backups:
        return

    response = input("\nRestore from latest backup? (yes/no): ").strip().lower()
    if response != "yes":
        print("Cancelled.")
        return

    print("\nStopping server (if running)...")
    import subprocess
    try:
        subprocess.run(["pkill", "-f", "python.*app"],
                      stderr=subprocess.DEVNULL,
                      stdout=subprocess.DEVNULL)
    except:
        pass  # Windows - pkill not available

    # Restore from latest backup
    if restore_from_backup(backups[0]):
        print("\n" + "=" * 60)
        print("     Restore complete!")
        print("=" * 60)
        print("\nTo restart the server:")
        print("  python app.py")
    else:
        print("\n✗ Restore failed. Database unchanged.")
        sys.exit(1)

if __name__ == "__main__":
    main()
