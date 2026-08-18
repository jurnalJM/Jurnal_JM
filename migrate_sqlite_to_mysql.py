#!/usr/bin/env python3
"""
One-off migration: copy all data from the local SQLite database into MySQL.

Usage:
    MYSQL_URL="mysql+pymysql://user:pass@host:3306/dbname?charset=utf8mb4" \
    python migrate_sqlite_to_mysql.py

MYSQL_URL is a required env var (no credentials are hardcoded here).
SQLITE_URL defaults to the project's local SQLite file but can also be
overridden. Creates the schema on the MySQL side if needed, then copies
every row table-by-table using SQLAlchemy Core (bulk insert, original
primary keys preserved).
"""

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from sqlalchemy import create_engine, inspect, text, MetaData

from database.models import Base

SQLITE_URL = os.environ.get("SQLITE_URL", "sqlite:///data/jaya_motor.db")
MYSQL_URL = os.environ.get("MYSQL_URL")

if not MYSQL_URL:
    print("ERROR: set the MYSQL_URL env var before running this script.")
    print("See the usage note at the top of this file.")
    sys.exit(1)

# Table copy order respects foreign-key dependencies (parents before children).
TABLE_ORDER = [
    "dealer",
    "broker",
    "leasing",
    "type_motor",
    "stok_motor",
    "transaksi",
    "transaksi_detail",
    "pembayaran_hutang",
    "dokumen",
    "catatan",
    "pembayaran",
    "stok_transfer",
    "admin_log",
]


def main():
    print(f"Source (SQLite): {SQLITE_URL}")
    print(f"Target (MySQL):  {MYSQL_URL.split('@')[-1]}\n")

    sqlite_engine = create_engine(SQLITE_URL)
    mysql_engine = create_engine(MYSQL_URL)

    # Make sure schema exists on the MySQL side (no-op if already created).
    Base.metadata.create_all(mysql_engine)

    metadata = MetaData()
    metadata.reflect(bind=sqlite_engine)

    known_tables = set(TABLE_ORDER)
    reflected_tables = set(metadata.tables.keys())
    missing_from_order = reflected_tables - known_tables
    if missing_from_order:
        print(f"WARNING: tables present in SQLite but not in TABLE_ORDER, skipping: {missing_from_order}")

    with mysql_engine.begin() as mysql_conn:
        mysql_conn.execute(text("SET FOREIGN_KEY_CHECKS=0"))

        for table_name in TABLE_ORDER:
            if table_name not in reflected_tables:
                print(f"  - {table_name}: not found in SQLite, skipping")
                continue

            table = metadata.tables[table_name]

            with sqlite_engine.connect() as sqlite_conn:
                rows = [dict(row._mapping) for row in sqlite_conn.execute(table.select())]

            if not rows:
                print(f"  - {table_name}: 0 rows")
                continue

            mysql_conn.execute(text(f"DELETE FROM `{table_name}`"))
            mysql_conn.execute(table.insert(), rows)
            print(f"  - {table_name}: {len(rows)} rows migrated")

        mysql_conn.execute(text("SET FOREIGN_KEY_CHECKS=1"))

    # Verify counts match on both sides
    print("\nVerification:")
    inspector = inspect(mysql_engine)
    mysql_tables = set(inspector.get_table_names())
    all_ok = True
    with sqlite_engine.connect() as sconn, mysql_engine.connect() as mconn:
        for table_name in TABLE_ORDER:
            if table_name not in reflected_tables or table_name not in mysql_tables:
                continue
            src_count = sconn.execute(text(f'SELECT COUNT(*) FROM "{table_name}"')).scalar()
            dst_count = mconn.execute(text(f"SELECT COUNT(*) FROM `{table_name}`")).scalar()
            status = "OK" if src_count == dst_count else "MISMATCH"
            if src_count != dst_count:
                all_ok = False
            print(f"  - {table_name}: sqlite={src_count} mysql={dst_count} [{status}]")

    print("\nMigration complete." if all_ok else "\nMigration finished WITH MISMATCHES - check above.")


if __name__ == "__main__":
    main()
