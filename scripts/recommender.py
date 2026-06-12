"""
Mutual Fund Recommendation Engine

This module recommends mutual funds based on the user's
risk category preference. Recommendations are generated
using the highest Sharpe Ratio values.

Datasets Used:
- 07_scheme_performance.csv
- 01_fund_master.csv
"""

import pandas as pd


def recommend_funds(risk_category):
    """
    Recommend the top 3 mutual funds for a given risk category.

    Parameters
    ----------
    risk_category : str
        User's preferred risk category.
        Examples:
        Low, Moderate, High, Moderately High, Very High

    Returns
    -------
    pandas.DataFrame
        Top 3 recommended funds sorted by Sharpe Ratio.
    """

    try:
        # Load datasets
        performance_data = pd.read_csv(
            "data/raw/07_scheme_performance.csv"
        )
        fund_master_data = pd.read_csv(
            "data/raw/01_fund_master.csv"
        )

        # Merge risk category information
        fund_data = performance_data.merge(
            fund_master_data[
                ['amfi_code', 'risk_category']
            ],
            on='amfi_code',
            how='left'
        )

        # Filter funds by risk category
        filtered_funds = fund_data[
            fund_data['risk_category'].str.lower()
            == risk_category.lower()
        ]

        # Select top 3 funds based on Sharpe Ratio
        recommended_funds = (
            filtered_funds
            .sort_values(
                by='sharpe_ratio',
                ascending=False
            )
            .head(3)
        )

        return recommended_funds[
            [
                'scheme_name',
                'fund_house',
                'risk_category',
                'sharpe_ratio',
                'return_3yr_pct'
            ]
        ]

    except FileNotFoundError:
        print("Error: Dataset files not found.")
        return pd.DataFrame()

    except Exception as error:
        print(f"An unexpected error occurred: {error}")
        return pd.DataFrame()


def main():
    """
    Execute the recommendation engine.
    """

    risk_category = input(
        "Enter risk category "
        "(Low/Moderate/High/Moderately High/Very High): "
    )

    recommendations = recommend_funds(risk_category)

    if recommendations.empty:
        print("\nNo recommendations found.")
    else:
        print("\nTop 3 Recommended Funds:\n")
        print(recommendations)


if __name__ == "__main__":
    main()