"""
Master execution script for Mutual Fund Analytics.
"""

from data_ingestion import inspect_datasets
from amfi_validation import validate_amfi_codes
from day2_cleaning import (
    clean_nav_history,
    clean_investor_transactions,
    clean_scheme_performance
)
from create_db import create_database
from load_data import (
    load_dim_fund,
    load_fact_nav,
    load_fact_transactions,
    load_fact_performance
)
from verify_db import verify_tables
from live_nav_fetch import fetch_live_nav


def main():
    print("=" * 60)
    print("MUTUAL FUND ANALYTICS PIPELINE")
    print("=" * 60)

    inspect_datasets()

    validate_amfi_codes()

    clean_nav_history()
    clean_investor_transactions()
    clean_scheme_performance()

    create_database()

    from sqlalchemy import create_engine

    engine = create_engine(
        "sqlite:///database/bluestock_mf.db"
    )

    load_dim_fund(engine)
    load_fact_nav(engine)
    load_fact_transactions(engine)
    load_fact_performance(engine)

    verify_tables()

    fetch_live_nav()

    print("\nPipeline executed successfully.")


if __name__ == "__main__":
    main()