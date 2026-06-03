# scripts/verify_db.py

import sqlite3

conn = sqlite3.connect(
    "database/bluestock_mf.db"
)

cur = conn.cursor()

tables = [
    "dim_fund",
    "fact_nav",
    "fact_transactions",
    "fact_performance"
]

for table in tables:
    cur.execute(
        f"SELECT COUNT(*) FROM {table}"
    )

    print(
        f"{table}:",
        cur.fetchone()[0]
    )

conn.close()