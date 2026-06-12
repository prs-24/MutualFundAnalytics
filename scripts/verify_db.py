"""
Database Verification Module

This module verifies that data has been successfully loaded
into the SQLite database by checking the row counts of all
fact and dimension tables.

Tables Verified:
- dim_fund
- fact_nav
- fact_transactions
- fact_performance
"""

import sqlite3


DATABASE_PATH = "database/bluestock_mf.db"

TABLES = [
    "dim_fund",
    "fact_nav",
    "fact_transactions",
    "fact_performance"
]


def verify_tables():
    """
    Verify the number of records present in each table.

    Returns
    -------
    None
    """

    try:
        with sqlite3.connect(DATABASE_PATH) as connection:

            cursor = connection.cursor()

            print("\nDatabase Verification Results")
            print("-" * 40)

            for table_name in TABLES:

                cursor.execute(
                    f"SELECT COUNT(*) FROM {table_name}"
                )

                row_count = cursor.fetchone()[0]

                print(
                    f"{table_name:<20}: {row_count:,} rows"
                )

    except sqlite3.Error as error:
        print(
            f"SQLite error occurred: {error}"
        )

    except Exception as error:
        print(
            f"An unexpected error occurred: {error}"
        )


def main():
    """
    Execute database verification.
    """

    verify_tables()


if __name__ == "__main__":
    main()