"""
Data Ingestion and Initial Validation Module

This module loads all raw CSV files from the data/raw directory
and performs a preliminary inspection, including:

- Dataset shape
- Column names
- Data types
- Missing values
- Duplicate rows
- Sample records

This helps assess data quality before cleaning and analysis.
"""

import os

import pandas as pd

DATA_FOLDER = "data/raw"


def inspect_datasets():
    """
    Inspect all CSV files present in the raw data folder.

    Returns
    -------
    None
    """

    try:
        csv_files = [
            file
            for file in os.listdir(DATA_FOLDER)
            if file.endswith(".csv")
        ]

        if not csv_files:
            print("No CSV files found in the data/raw directory.")
            return

        for file_name in csv_files:

            file_path = os.path.join(DATA_FOLDER, file_name)

            print("\n" + "=" * 60)
            print(f"FILE: {file_name}")

            dataset = pd.read_csv(file_path)

            print(f"\nShape: {dataset.shape}")

            print("\nColumns:")
            print(dataset.columns.tolist())

            print("\nData Types:")
            print(dataset.dtypes)

            print("\nMissing Values:")
            print(dataset.isnull().sum())

            print("\nDuplicate Rows:")
            print(dataset.duplicated().sum())

            print("\nFirst Five Records:")
            print(dataset.head())

    except FileNotFoundError:
        print(f"Error: Directory '{DATA_FOLDER}' not found.")

    except Exception as error:
        print(f"An unexpected error occurred: {error}")


def main():
    """
    Execute the data ingestion and inspection process.
    """
    inspect_datasets()


if __name__ == "__main__":
    main()