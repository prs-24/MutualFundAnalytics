import pandas as pd

# Load datasets
performance = pd.read_csv("data/raw/07_scheme_performance.csv")
fund_master = pd.read_csv("data/raw/01_fund_master.csv")

# Merge risk category information
funds = performance.merge(
    fund_master[['amfi_code', 'risk_category']],
    on='amfi_code',
    how='left'
)

# User input
risk = input(
    "Enter risk category (Low/Moderate/High/Moderately High/Very High): "
)

# Filter funds
filtered = funds[
    funds['risk_category'].str.lower() == risk.lower()
]

# Top 3 funds by Sharpe Ratio
recommendations = (
    filtered
    .sort_values('sharpe_ratio', ascending=False)
    .head(3)
)

print("\nTop 3 Recommended Funds:\n")

print(
    recommendations[
        [
            'scheme_name',
            'fund_house',
            'risk_category',
            'sharpe_ratio',
            'return_3yr_pct'
        ]
    ]
)