"""
AMFI Code Validation Module

This module validates whether all AMFI codes present in the
Fund Master dataset are available in the NAV History dataset.

The validation helps ensure referential integrity between
datasets and identifies any missing or unmatched codes.
"""

import pandas as pd


def validate_amfi_codes():
    """
    Validate AMFI codes between Fund Master and NAV History datasets.

    Returns
    -------
    set
        Set of AMFI codes present in Fund Master but missing from
        NAV History.
    """

    fund_master_data = pd.read_csv(
        "data/raw/01_fund_master.csv"
    )

    nav_history_data = pd.read_csv(
        "data/raw/02_nav_history.csv"
    )

    fund_codes = set(
        fund_master_data["amfi_code"]
    )

    nav_codes = set(
        nav_history_data["amfi_code"]
    )

    missing_codes = fund_codes - nav_codes

    print(f"Fund Master Codes: {len(fund_codes)}")
    print(f"NAV History Codes: {len(nav_codes)}")
    print(f"Missing Codes: {len(missing_codes)}")

    if missing_codes:
        print("\nMissing AMFI Codes:")
        print(missing_codes)
    else:
        print(
            "\nAll AMFI codes validated successfully."
        )

    return missing_codes


def main():
    """
    Execute AMFI code validation.
    """

    try:
        validate_amfi_codes()

    except FileNotFoundError:
        print(
            "Error: One or more dataset files were not found."
        )

    except Exception as error:
        print(
            f"An unexpected error occurred: {error}"
        )


if __name__ == "__main__":
    main()