"""
Database Loading Module

Loads cleaned and transformed datasets into the SQLite
database tables for the Mutual Fund Analytics project.

Tables Loaded:
- dim_fund
- fact_nav
- fact_transactions
- fact_performance
"""

from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine


DATABASE_URL = "sqlite:///database/bluestock_mf.db"

RAW_DATA_PATH = Path("data/raw")
PROCESSED_DATA_PATH = Path("data/processed")


def load_dim_fund(engine):
    """
    Load fund master data into the dim_fund table.
    """

    fund_data = pd.read_csv(
        RAW_DATA_PATH / "01_fund_master.csv"
    )

    fund_data = fund_data[
        [
            "amfi_code",
            "scheme_name",
            "fund_house",
            "category",
            "sub_category",
            "fund_manager"
        ]
    ]

    fund_data.to_sql(
        "dim_fund",
        engine,
        if_exists="append",
        index=False
    )

    print("dim_fund loaded successfully.")


def load_fact_nav(engine):
    """
    Load NAV history into the fact_nav table.
    """

    nav_data = pd.read_csv(
        PROCESSED_DATA_PATH /
        "02_nav_history_clean.csv"
    )

    nav_data.rename(
        columns={"date": "nav_date"},
        inplace=True
    )

    nav_data.to_sql(
        "fact_nav",
        engine,
        if_exists="append",
        index=False
    )

    print("fact_nav loaded successfully.")


def load_fact_transactions(engine):
    """
    Load investor transactions into the fact_transactions table.
    """

    transaction_data = pd.read_csv(
        PROCESSED_DATA_PATH /
        "08_investor_transactions_clean.csv"
    )

    transaction_data = transaction_data[
        [
            "investor_id",
            "amfi_code",
            "transaction_date",
            "transaction_type",
            "amount_inr",
            "state",
            "city",
            "kyc_status"
        ]
    ]

    transaction_data.to_sql(
        "fact_transactions",
        engine,
        if_exists="append",
        index=False
    )

    print("fact_transactions loaded successfully.")


def load_fact_performance(engine):
    """
    Load scheme performance metrics into the fact_performance table.
    """

    performance_data = pd.read_csv(
        PROCESSED_DATA_PATH /
        "07_scheme_performance_clean.csv"
    )

    performance_data = performance_data[
        [
            "amfi_code",
            "return_1yr_pct",
            "return_3yr_pct",
            "return_5yr_pct",
            "sharpe_ratio",
            "expense_ratio_pct",
            "aum_crore"
        ]
    ]

    performance_data.to_sql(
        "fact_performance",
        engine,
        if_exists="append",
        index=False
    )

    print("fact_performance loaded successfully.")


def main():
    """
    Execute database loading process.
    """

    try:
        engine = create_engine(
            DATABASE_URL
        )

        load_dim_fund(engine)
        load_fact_nav(engine)
        load_fact_transactions(engine)
        load_fact_performance(engine)

        print(
            "\nAll tables loaded successfully."
        )

    except FileNotFoundError:
        print(
            "Error: One or more input files were not found."
        )

    except Exception as error:
        print(
            f"An unexpected error occurred: {error}"
        )


if __name__ == "__main__":
    main()