import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///database/bluestock_mf.db"
)

# ---------------------
# DIM FUND
# ---------------------

fund = pd.read_csv(
    "data/raw/01_fund_master.csv"
)

fund = fund[
    [
        "amfi_code",
        "scheme_name",
        "fund_house",
        "category",
        "sub_category",
        "fund_manager"
    ]
]

fund.to_sql(
    "dim_fund",
    engine,
    if_exists="append",
    index=False
)

print("dim_fund loaded")

# ---------------------
# FACT NAV
# ---------------------

nav = pd.read_csv(
    "data/processed/02_nav_history_clean.csv"
)

nav.rename(
    columns={
        "date": "nav_date"
    },
    inplace=True
)

nav.to_sql(
    "fact_nav",
    engine,
    if_exists="append",
    index=False
)

print("fact_nav loaded")

# ---------------------
# FACT TRANSACTIONS
# ---------------------

txn = pd.read_csv(
    "data/processed/08_investor_transactions_clean.csv"
)
txn = txn[
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
txn.to_sql(
    "fact_transactions",
    engine,
    if_exists="append",
    index=False
)

print("fact_transactions loaded")

# ---------------------
# FACT PERFORMANCE
# ---------------------

perf = pd.read_csv(
    "data/processed/07_scheme_performance_clean.csv"
)

perf = perf[
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

perf.to_sql(
    "fact_performance",
    engine,
    if_exists="append",
    index=False
)

print("fact_performance loaded")