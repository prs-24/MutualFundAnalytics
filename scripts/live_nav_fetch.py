"""
Live NAV Data Fetch Module

Fetches historical NAV data for a mutual fund from the MFAPI
service and stores it as a CSV file for further analysis.

API Source:
https://api.mfapi.in/
"""

from pathlib import Path

import pandas as pd
import requests


FUND_CODE = 125497
API_URL = f"https://api.mfapi.in/mf/{FUND_CODE}"
OUTPUT_FILE = Path("data/raw/live_hdfc_top100_nav.csv")


def fetch_live_nav() -> pd.DataFrame:
    """
    Retrieve NAV history for the specified mutual fund.

    Returns
    -------
    pandas.DataFrame
        DataFrame containing NAV records. Returns an empty
        DataFrame if data retrieval fails.
    """

    try:
        response = requests.get(
            API_URL,
            timeout=10
        )
        response.raise_for_status()

        response_data = response.json()

        nav_records = response_data.get("data")

        if not nav_records:
            print("No NAV data found in API response.")
            return pd.DataFrame()

        nav_data = pd.DataFrame(nav_records)

        # Ensure output directory exists
        OUTPUT_FILE.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        nav_data.to_csv(
            OUTPUT_FILE,
            index=False
        )

        print(
            f"Successfully saved "
            f"{len(nav_data)} records to "
            f"'{OUTPUT_FILE}'."
        )

        return nav_data

    except requests.exceptions.RequestException as error:
        print(
            f"Error fetching NAV data: {error}"
        )

    except ValueError:
        print(
            "Error decoding JSON response."
        )

    except Exception as error:
        print(
            f"Unexpected error: {error}"
        )

    return pd.DataFrame()


def main() -> None:
    """
    Execute live NAV data retrieval.
    """

    fetch_live_nav()


if __name__ == "__main__":
    main()