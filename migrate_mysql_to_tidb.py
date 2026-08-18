#!/usr/bin/env python3
"""
One-off migration: copy all data from local MySQL into TiDB Cloud.

Usage:
    SOURCE_URL="mysql+pymysql://user:pass@host:3306/dbname?charset=utf8mb4" \
    TARGET_URL="mysql+pymysql://user:pass@gatewayXX.<region>.prod.aws.tidbcloud.com:4000/dbname?charset=utf8mb4" \
    python migrate_mysql_to_tidb.py

Both SOURCE_URL and TARGET_URL are required env vars (no credentials are
hardcoded here). Creates the schema on the TiDB side if needed, then copies
every row table-by-table using SQLAlchemy Core (bulk insert, original
primary keys preserved).
"""

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import certifi
from sqlalchemy import create_engine, inspect, text, MetaData

from database.models import Base

SOURCE_URL = os.environ.get("SOURCE_URL")
TARGET_URL = os.environ.get("TARGET_URL")

if not SOURCE_URL or not TARGET_URL:
    print("ERROR: set SOURCE_URL and TARGET_URL env vars before running this script.")
    print("See the usage note at the top of this file.")
    sys.exit(1)

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
    print(f"Source: {SOURCE_URL.split('@')[-1]}")
    print(f"Target: {TARGET_URL.split('@')[-1]}\n")

    source_engine = create_engine(SOURCE_URL)
    target_engine = create_engine(
        TARGET_URL,
        connect_args={
            "ssl_ca": certifi.where(),
            "ssl_verify_cert": True,
            "ssl_verify_identity": True,
        },
    )

    # Make sure schema exists on the TiDB side (no-op if already created).
    Base.metadata.create_all(target_engine)

    metadata = MetaData()
    metadata.reflect(bind=source_engine)

    reflected_tables = set(metadata.tables.keys())

    with target_engine.begin() as target_conn:
        target_conn.execute(text("SET FOREIGN_KEY_CHECKS=0"))

        for table_name in TABLE_ORDER:
            if table_name not in reflected_tables:
                print(f"  - {table_name}: not found in source, skipping")
                continue

            table = metadata.tables[table_name]

            with source_engine.connect() as source_conn:
                rows = [dict(row._mapping) for row in source_conn.execute(table.select())]

            if not rows:
                print(f"  - {table_name}: 0 rows")
                continue

            target_conn.execute(text(f"DELETE FROM `{table_name}`"))
            target_conn.execute(table.insert(), rows)
            print(f"  - {table_name}: {len(rows)} rows migrated")

        target_conn.execute(text("SET FOREIGN_KEY_CHECKS=1"))

    print("\nVerification:")
    target_tables = set(inspect(target_engine).get_table_names())
    all_ok = True
    with source_engine.connect() as sconn, target_engine.connect() as tconn:
        for table_name in TABLE_ORDER:
            if table_name not in reflected_tables or table_name not in target_tables:
                continue
            src_count = sconn.execute(text(f"SELECT COUNT(*) FROM `{table_name}`")).scalar()
            dst_count = tconn.execute(text(f"SELECT COUNT(*) FROM `{table_name}`")).scalar()
            status = "OK" if src_count == dst_count else "MISMATCH"
            if src_count != dst_count:
                all_ok = False
            print(f"  - {table_name}: source={src_count} target={dst_count} [{status}]")

    print("\nMigration complete." if all_ok else "\nMigration finished WITH MISMATCHES - check above.")


if __name__ == "__main__":
    main()
