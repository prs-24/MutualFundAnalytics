-- =====================================================
-- Query 1: Top 5 Fund Houses by Total AUM
-- =====================================================

SELECT
    df.fund_house,
    SUM(fp.aum_crore) AS total_aum
FROM fact_performance fp
JOIN dim_fund df
ON fp.amfi_code = df.amfi_code
GROUP BY df.fund_house
ORDER BY total_aum DESC
LIMIT 5;

-- =====================================================
-- Query 2: Average 3-Year Return by Category
-- =====================================================

SELECT
    df.category,
    ROUND(AVG(fp.return_3yr_pct),2) AS avg_return_3yr
FROM fact_performance fp
JOIN dim_fund df
ON fp.amfi_code = df.amfi_code
GROUP BY df.category
ORDER BY avg_return_3yr DESC;

-- =====================================================
-- Query 3: Transaction Count by Type
-- =====================================================

SELECT
    transaction_type,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY transaction_type;

-- =====================================================
-- Query 4: Top States by Investment Amount
-- =====================================================

SELECT
    state,
    ROUND(SUM(amount_inr),2) AS total_investment
FROM fact_transactions
GROUP BY state
ORDER BY total_investment DESC;

-- =====================================================
-- Query 5: Average NAV Across All Funds
-- =====================================================

SELECT
    ROUND(AVG(nav),4) AS average_nav
FROM fact_nav;

-- =====================================================
-- Query 6: Average Expense Ratio by Category
-- =====================================================

SELECT
    df.category,
    ROUND(AVG(fp.expense_ratio_pct),2) AS avg_expense_ratio
FROM fact_performance fp
JOIN dim_fund df
ON fp.amfi_code = df.amfi_code
GROUP BY df.category
ORDER BY avg_expense_ratio DESC;

-- =====================================================
-- Query 7: Top 10 Funds by 5-Year Return
-- =====================================================

SELECT
    df.scheme_name,
    fp.return_5yr_pct
FROM fact_performance fp
JOIN dim_fund df
ON fp.amfi_code = df.amfi_code
ORDER BY fp.return_5yr_pct DESC
LIMIT 10;

-- =====================================================
-- Query 8: KYC Status Distribution
-- =====================================================

SELECT
    kyc_status,
    COUNT(*) AS investors
FROM fact_transactions
GROUP BY kyc_status;

-- =====================================================
-- Query 9: Number of Schemes per Fund House
-- =====================================================

SELECT
    fund_house,
    COUNT(*) AS total_schemes
FROM dim_fund
GROUP BY fund_house
ORDER BY total_schemes DESC;

-- =====================================================
-- Query 10: Top 10 Funds by Sharpe Ratio
-- =====================================================

SELECT
    df.scheme_name,
    fp.sharpe_ratio
FROM fact_performance fp
JOIN dim_fund df
ON fp.amfi_code = df.amfi_code
ORDER BY fp.sharpe_ratio DESC
LIMIT 10;