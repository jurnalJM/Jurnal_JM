#!/usr/bin/env python3
"""
Export all data from the current DATABASE_URL (.env) into a single JSON file.
Used to move data across networks that can't reach each other directly
(e.g. TiDB Cloud -> a file you upload into PythonAnywhere's Files tab).

Usage:
    python export_tidb_to_json.py [output_file.json]
"""

import sys
import json
from pathlib import Path
from decimal import Decimal
from datetime import date, datetime

sys.path.insert(0, str(Path(__file__).parent))

from sqlalchemy import create_engine, MetaData

from config import DATABASE_URL, DB_SSL_REQUIRED

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


def default_serializer(obj):
    if isinstance(obj, (date, datetime)):
        return obj.isoformat()
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError(f"Not serializable: {type(obj)}")


def main():
    out_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("data_export.json")

    connect_args = {}
    if DB_SSL_REQUIRED:
        import certifi

        connect_args = {
            "ssl_ca": certifi.where(),
            "ssl_verify_cert": True,
            "ssl_verify_identity": True,
        }

    print(f"Source: {DATABASE_URL.split('@')[-1]}")
    engine = create_engine(DATABASE_URL, connect_args=connect_args)

    metadata = MetaData()
    metadata.reflect(bind=engine)
    reflected_tables = set(metadata.tables.keys())

    dump = {}
    with engine.connect() as conn:
        for table_name in TABLE_ORDER:
            if table_name not in reflected_tables:
                continue
            table = metadata.tables[table_name]
            rows = [dict(row._mapping) for row in conn.execute(table.select())]
            dump[table_name] = rows
            print(f"  - {table_name}: {len(rows)} rows")

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(dump, f, default=default_serializer, ensure_ascii=False)

    print(f"\nWrote {out_path} ({out_path.stat().st_size / 1024:.1f} KB)")


if __name__ == "__main__":
    main()
