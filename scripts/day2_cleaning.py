import pandas as pd
import os

RAW = "data/raw"
PROCESSED = "data/processed"

os.makedirs(PROCESSED, exist_ok=True)

# -----------------------
# NAV HISTORY
# -----------------------

nav = pd.read_csv(f"{RAW}/02_nav_history.csv")

nav["date"] = pd.to_datetime(nav["date"])

nav = nav.sort_values(
    ["amfi_code", "date"]
)

nav = nav.drop_duplicates()

nav = nav[nav["nav"] > 0]

nav.to_csv(
    f"{PROCESSED}/02_nav_history_clean.csv",
    index=False
)

print("NAV cleaned")

# -----------------------
# INVESTOR TRANSACTIONS
# -----------------------

txn = pd.read_csv(
    f"{RAW}/08_investor_transactions.csv"
)

txn["transaction_date"] = pd.to_datetime(
    txn["transaction_date"]
)

txn["transaction_type"] = (
    txn["transaction_type"]
    .str.strip()
    .str.title()
)

valid_types = [
    "Sip",
    "Lumpsum",
    "Redemption"
]

txn = txn[
    txn["transaction_type"]
    .isin(valid_types)
]

txn = txn[
    txn["amount_inr"] > 0
]

txn.to_csv(
    f"{PROCESSED}/08_investor_transactions_clean.csv",
    index=False
)

print("Transactions cleaned")

# -----------------------
# SCHEME PERFORMANCE
# -----------------------

perf = pd.read_csv(
    f"{RAW}/07_scheme_performance.csv"
)

perf = perf[
    (perf["expense_ratio_pct"] >= 0.1)
    &
    (perf["expense_ratio_pct"] <= 2.5)
]

perf.to_csv(
    f"{PROCESSED}/07_scheme_performance_clean.csv",
    index=False
)

print("Performance cleaned")