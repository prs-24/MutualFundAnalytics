# Mutual Fund Analytics - Data Dictionary

## dim_fund

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | INTEGER | Unique AMFI scheme identifier |
| scheme_name | TEXT | Name of mutual fund scheme |
| fund_house | TEXT | Asset Management Company |
| category | TEXT | Fund category |
| sub_category | TEXT | Fund sub-category |
| fund_manager | TEXT | Fund manager |

---

## fact_nav

| Column | Type | Description |
|----------|----------|----------|
| nav_id | INTEGER | Primary key |
| amfi_code | INTEGER | Fund identifier |
| nav_date | DATE | NAV date |
| nav | REAL | Net Asset Value |

---

## fact_transactions

| Column | Type | Description |
|----------|----------|----------|
| transaction_id | INTEGER | Primary key |
| investor_id | TEXT | Investor ID |
| amfi_code | INTEGER | Fund identifier |
| transaction_date | DATE | Transaction date |
| transaction_type | TEXT | SIP / Lumpsum / Redemption |
| amount_inr | REAL | Transaction amount |
| state | TEXT | Investor state |
| city | TEXT | Investor city |
| kyc_status | TEXT | KYC verification status |

---

## fact_performance

| Column | Type | Description |
|----------|----------|----------|
| performance_id | INTEGER | Primary key |
| amfi_code | INTEGER | Fund identifier |
| return_1yr_pct | REAL | 1-Year Return |
| return_3yr_pct | REAL | 3-Year Return |
| return_5yr_pct | REAL | 5-Year Return |
| sharpe_ratio | REAL | Risk-adjusted return metric |
| expense_ratio_pct | REAL | Expense ratio |
| aum_crore | REAL | Assets Under Management |