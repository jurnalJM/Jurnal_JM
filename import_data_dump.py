#!/usr/bin/env python3
"""
Import a JSON data dump (produced by export_tidb_to_json.py) into whatever
database DATABASE_URL (.env) currently points to. Used to move data across
networks that can't reach each other directly (e.g. into PythonAnywhere's
own MySQL, which can't be reached from outside their infrastructure).

This REPLACES existing rows in each table (delete then insert), so double
check DATABASE_URL before confirming.

Usage:
    python import_data_dump.py [data_export.json]
"""

import sys
import json
from pathlib import Path
from datetime import date, datetime

sys.path.insert(0, str(Path(__file__).parent))

from sqlalchemy import create_engine, text
from sqlalchemy.types import Date, DateTime

from config import DATABASE_URL, DB_SSL_REQUIRED
from database.models import Base

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


def coerce_row(table, row):
    result = {}
    for col in table.columns:
        val = row.get(col.name)
        if isinstance(val, str):
            if isinstance(col.type, DateTime):
                val = datetime.fromisoformat(val)
            elif isinstance(col.type, Date):
                val = date.fromisoformat(val)
        result[col.name] = val
    return result


def main():
    dump_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("data_export.json")
    if not dump_path.exists():
        print(f"ERROR: {dump_path} not found. Upload the exported JSON file first.")
        sys.exit(1)

    with open(dump_path, encoding="utf-8") as f:
        dump = json.load(f)

    print(f"Target: {DATABASE_URL.split('@')[-1]}")
    confirm = input("This will REPLACE data in the tables above. Type 'yes' to continue: ")
    if confirm.strip().lower() != "yes":
        print("Aborted.")
        sys.exit(0)

    connect_args = {}
    if DB_SSL_REQUIRED:
        import certifi

        connect_args = {
            "ssl_ca": certifi.where(),
            "ssl_verify_cert": True,
            "ssl_verify_identity": True,
        }

    engine = create_engine(DATABASE_URL, connect_args=connect_args)
    Base.metadata.create_all(engine)

    with engine.begin() as conn:
        conn.execute(text("SET FOREIGN_KEY_CHECKS=0"))
        for table_name in TABLE_ORDER:
            if table_name not in dump:
                continue
            table = Base.metadata.tables[table_name]
            rows = [coerce_row(table, r) for r in dump[table_name]]
            conn.execute(text(f"DELETE FROM `{table_name}`"))
            if rows:
                conn.execute(table.insert(), rows)
            print(f"  - {table_name}: {len(rows)} rows imported")
        conn.execute(text("SET FOREIGN_KEY_CHECKS=1"))

    print("\nImport complete.")


if __name__ == "__main__":
    main()
