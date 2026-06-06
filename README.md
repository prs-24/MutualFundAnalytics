# Mutual Fund Analytics – Capstone Project

## Overview

Mutual Fund Analytics is an end-to-end data engineering and analytics project focused on analyzing mutual fund performance, investor behavior, AUM trends, SIP inflows, portfolio holdings, benchmark indices, and fund risk-adjusted returns.

The project covers the complete analytics lifecycle including data ingestion, validation, cleaning, database design, exploratory data analysis (EDA), performance analytics, risk metrics, business insight generation, and dashboard-ready data preparation.

---

## Project Objectives

* Collect and validate mutual fund datasets
* Perform data quality assessment and cleaning
* Standardize and validate financial data
* Design a structured SQLite analytics database
* Generate business insights using SQL queries
* Perform Exploratory Data Analysis (EDA)
* Analyze fund performance and risk metrics
* Compare funds against benchmark indices
* Build reusable data pipelines for reporting and dashboarding
* Prepare analytics-ready datasets for visualization

---

# Day 1: Data Ingestion & Validation

## Objectives

* Project setup and repository initialization
* Data ingestion and profiling
* Data quality assessment
* AMFI code validation
* Live NAV data fetching using MFAPI

## Deliverables

* `data_ingestion.py`
* `amfi_validation.py`
* `live_nav_fetch.py`
* `data_quality_summary.txt`

## Key Activities

* Loaded and profiled all source datasets
* Performed dataset validation checks
* Validated AMFI codes
* Integrated live NAV fetching using MFAPI
* Generated data quality summary reports

---

# Day 2: Data Cleaning & SQLite Database Design

## Data Cleaning

Performed cleaning and validation on:

* NAV History Dataset
* Investor Transactions Dataset
* Scheme Performance Dataset

### NAV History

* Date conversion and standardization
* Sorting by AMFI code and date
* Duplicate removal
* Missing value handling
* NAV > 0 validation

### Investor Transactions

* Transaction date standardization
* Transaction type standardization
* Amount validation
* KYC status validation
* Missing value handling

### Scheme Performance

* Return metric validation
* Expense ratio validation
* Performance metric consistency checks

---

## Database Design

### Dimension Tables

* `dim_fund`

### Fact Tables

* `fact_nav`
* `fact_transactions`
* `fact_performance`

---

## Database Statistics

| Table             | Records |
| ----------------- | ------: |
| dim_fund          |      40 |
| fact_nav          |  46,000 |
| fact_transactions |  32,778 |
| fact_performance  |      40 |

---

## SQL Analytics Implemented

* Top Fund Houses by AUM
* Average Returns by Category
* Transaction Analysis by Type
* State-wise Investment Analysis
* Average NAV Analysis
* Expense Ratio Comparison
* Top Funds by 5-Year Returns
* KYC Status Distribution
* Fund House Scheme Count
* Top Funds by Sharpe Ratio

---

# Day 3: Exploratory Data Analysis (EDA)

## Objectives

* Dataset profiling and exploration
* NAV trend analysis
* AUM growth analysis
* SIP inflow analysis
* Category inflow analysis
* Investor demographic analysis
* Geographic investment analysis
* Folio growth analysis
* Portfolio allocation analysis
* Benchmark index analysis
* Fund correlation analysis

---

## Visualizations Created

* NAV Trend Analysis
* AUM Growth Analysis
* SIP Inflow Trend
* Category Inflow Heatmap
* Age Group Distribution
* Gender Distribution
* Investment Amount Analysis
* State-wise Investment Distribution
* City Tier Distribution
* Folio Growth Trend
* Sector Allocation Donut Chart
* Benchmark Performance Analysis
* NAV Correlation Matrix

---

## Key Insights

* Mutual fund NAVs exhibited strong long-term growth trends.
* SIP inflows increased consistently throughout the analysis period.
* Folio growth indicates rising retail investor participation.
* AUM remains concentrated among leading fund houses.
* Investor participation varies significantly across age groups and geographies.
* Equity-oriented investment categories attracted stronger inflows.
* Sector allocation highlights concentration in key growth sectors.
* Benchmark indices demonstrated long-term market expansion despite periodic corrections.

---

# Day 4: Fund Performance Analytics & Risk Metrics

## Objectives

* Calculate daily fund returns
* Measure long-term growth using CAGR
* Evaluate risk-adjusted returns using Sharpe Ratio
* Evaluate downside-risk performance using Sortino Ratio
* Measure Alpha and Beta against NIFTY100 benchmark
* Analyze Maximum Drawdown
* Build a composite Fund Scorecard
* Compare top-performing funds with benchmark indices

---

## Performance Metrics Calculated

### Daily Returns

Calculated daily NAV returns for all schemes:

Daily Return = (NAVₜ / NAVₜ₋₁) − 1

### CAGR (Compound Annual Growth Rate)

Computed long-term annualized growth for all mutual funds.

### Sharpe Ratio

Measured risk-adjusted performance using:

Sharpe Ratio = (Rp − Rf) / σp

Risk-free rate used: **6.5%**

### Sortino Ratio

Measured downside-risk-adjusted performance using negative return volatility.

### Alpha & Beta

Performed benchmark comparison using:

* Benchmark: NIFTY100
* Linear Regression (`scipy.stats.linregress`)

Calculated:

* Alpha
* Beta

### Maximum Drawdown

Measured the largest peak-to-trough decline for each fund.

### Fund Scorecard

Generated a weighted scoring model using:

| Metric                | Weight |
| --------------------- | -----: |
| CAGR Rank             |    30% |
| Sharpe Rank           |    25% |
| Alpha Rank            |    20% |
| Expense Ratio Rank    |    15% |
| Maximum Drawdown Rank |    10% |

Generated:

* Fund Scores (0–100)
* Fund Rankings

---

## Visualizations Created

* Daily Return Distribution
* Top 5 Funds vs NIFTY100 Benchmark Comparison

---

## Deliverables

* `performance_analytics.ipynb`
* `cagr_results.csv`
* `alpha_beta.csv`
* `fund_scorecard.csv`
* `daily_returns_distribution.png`
* `benchmark_comparison.png`

---

## Datasets Used

1. Fund Master
2. NAV History
3. AUM by Fund House
4. Monthly SIP Inflows
5. Category Inflows
6. Industry Folio Count
7. Scheme Performance
8. Investor Transactions
9. Portfolio Holdings
10. Benchmark Indices

---

## Project Structure

```text
MutualFundAnalytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── database/
│   └── bluestock_mf.db
│
├── docs/
│   └── data_dictionary.md
│
├── notebooks/
│   ├── EDA_Analysis.ipynb
│   └── performance_analytics.ipynb
│
├── reports/
│   ├── alpha_beta.csv
│   ├── cagr_results.csv
│   ├── fund_scorecard.csv
│   ├── data_quality_summary.txt
│   └── charts/
│       ├── daily_returns_distribution.png
│       └── benchmark_comparison.png
│
├── scripts/
│   ├── data_ingestion.py
│   ├── amfi_validation.py
│   ├── live_nav_fetch.py
│   ├── day2_cleaning.py
│   ├── create_db.py
│   ├── load_data.py
│   └── verify_db.py
│
├── sql/
├── README.md
└── requirements.txt
```

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* SciPy
* Seaborn
* Plotly
* SQLite
* SQLAlchemy
* Requests
* Jupyter Notebook
* Git & GitHub

---

## Current Status

✅ Day 1 Completed – Data Ingestion & Validation

✅ Day 2 Completed – Data Cleaning & Database Design

✅ Day 3 Completed – Exploratory Data Analysis

✅ Day 4 Completed – Fund Performance Analytics & Risk Metrics

⏳ Day 5 – Dashboard Development & KPI Monitoring

⏳ Day 6 – Final Reporting, Documentation & Project Packaging

---

## Key Achievements

* Data ingestion pipeline implemented
* AMFI validation completed
* Live NAV integration completed
* Data cleaning pipeline developed
* SQLite analytics database designed and populated
* Business-focused SQL analytics implemented
* Exploratory Data Analysis completed
* Risk and return analytics completed
* Fund ranking and scorecard framework developed
* Benchmark comparison analytics implemented
* Dashboard-ready datasets prepared

---

## Next Steps

### Day 5

* Dashboard Development
* KPI Cards
* Fund Ranking Dashboard
* Benchmark Tracking Dashboard
* Investor Analytics Dashboard
* AUM & SIP Monitoring Dashboard

### Day 6

* Final Reporting
* Project Documentation
* Architecture Diagram
* Dashboard Screenshots
* GitHub Repository Cleanup
* Final Submission Package

```
```
