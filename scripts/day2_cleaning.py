"""
Data Cleaning Module

This module performs data cleaning and preprocessing on
selected datasets and saves the cleaned datasets to the
data/processed directory.

Datasets Processed:
- NAV History
- Investor Transactions
- Scheme Performance
"""

import os

import pandas as pd

RAW_FOLDER = "data/raw"
PROCESSED_FOLDER = "data/processed"

os.makedirs(PROCESSED_FOLDER, exist_ok=True)


def clean_nav_history():
    """
    Clean the NAV history dataset.

    Operations performed:
    - Convert date column to datetime
    - Sort records
    - Remove duplicates
    - Remove invalid NAV values

    Returns
    -------
    None
    """

    nav_data = pd.read_csv(
        f"{RAW_FOLDER}/02_nav_history.csv"
    )

    nav_data["date"] = pd.to_datetime(
        nav_data["date"]
    )

    nav_data = nav_data.sort_values(
        by=["amfi_code", "date"]
    )

    nav_data = nav_data.drop_duplicates()

    nav_data = nav_data[
        nav_data["nav"] > 0
    ]

    nav_data.to_csv(
        f"{PROCESSED_FOLDER}/02_nav_history_clean.csv",
        index=False
    )

    print("NAV history dataset cleaned successfully.")


def clean_investor_transactions():
    """
    Clean the investor transactions dataset.

    Operations performed:
    - Convert transaction date to datetime
    - Standardize transaction types
    - Filter valid transaction categories
    - Remove records with invalid amounts

    Returns
    -------
    None
    """

    transaction_data = pd.read_csv(
        f"{RAW_FOLDER}/08_investor_transactions.csv"
    )

    transaction_data["transaction_date"] = pd.to_datetime(
        transaction_data["transaction_date"]
    )

    transaction_data["transaction_type"] = (
        transaction_data["transaction_type"]
        .str.strip()
        .str.title()
    )

    valid_transaction_types = [
        "Sip",
        "Lumpsum",
        "Redemption"
    ]

    transaction_data = transaction_data[
        transaction_data["transaction_type"]
        .isin(valid_transaction_types)
    ]

    transaction_data = transaction_data[
        transaction_data["amount_inr"] > 0
    ]

    transaction_data.to_csv(
        f"{PROCESSED_FOLDER}/08_investor_transactions_clean.csv",
        index=False
    )

    print("Investor transactions dataset cleaned successfully.")


def clean_scheme_performance():
    """
    Clean the scheme performance dataset.

    Operations performed:
    - Remove unrealistic expense ratio values

    Returns
    -------
    None
    """

    performance_data = pd.read_csv(
        f"{RAW_FOLDER}/07_scheme_performance.csv"
    )

    performance_data = performance_data[
        (
            performance_data["expense_ratio_pct"] >= 0.1
        )
        &
        (
            performance_data["expense_ratio_pct"] <= 2.5
        )
    ]

    performance_data.to_csv(
        f"{PROCESSED_FOLDER}/07_scheme_performance_clean.csv",
        index=False
    )

    print("Scheme performance dataset cleaned successfully.")


def main():
    """
    Execute all data cleaning operations.
    """

    try:
        clean_nav_history()
        clean_investor_transactions()
        clean_scheme_performance()

        print("\nData cleaning completed successfully.")

    except FileNotFoundError:
        print("Error: One or more input files were not found.")

    except Exception as error:
        print(f"An unexpected error occurred: {error}")


if __name__ == "__main__":
    main()