# Mutual Fund Analytics – Capstone Project

## Overview

Mutual Fund Analytics is an end-to-end data engineering and analytics project focused on analyzing mutual fund performance, investor behavior, AUM trends, SIP inflows, portfolio holdings, and benchmark indices.

The project covers the complete analytics lifecycle including data ingestion, validation, cleaning, database design, exploratory data analysis, business insight generation, and dashboard-ready data preparation.

---

## Project Objectives

* Collect and validate mutual fund datasets
* Perform data quality assessment and cleaning
* Standardize and validate financial data
* Design a structured SQLite analytics database
* Generate business insights using SQL queries
* Perform Exploratory Data Analysis (EDA)
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

---

# Day 2: Data Cleaning & SQLite Database Design

## Data Cleaning

Performed cleaning and validation on:

* NAV History Dataset
* Investor Transactions Dataset
* Scheme Performance Dataset

### Validation Rules

#### NAV History

* Date conversion to datetime
* Sorting by AMFI code and date
* Duplicate removal
* NAV > 0 validation

#### Investor Transactions

* Transaction date standardization
* Transaction type standardization
* Amount validation
* KYC status validation

#### Scheme Performance

* Return metric validation
* Expense ratio validation
* Data consistency checks

---

## Database Design

### Dimension Table

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

## Analytical SQL Queries

Implemented analytical queries including:

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
* Category inflow visualization
* Investor demographic analysis
* Geographic distribution analysis
* Folio growth analysis
* Portfolio sector allocation analysis
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

## Datasets

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
│   ├── bluestock_mf.db
│   ├── schema.sql
│   └── queries.sql
│
├── docs/
│   └── data_dictionary.md
│
├── notebooks/
│   └── EDA_Analysis.ipynb
│
├── reports/
│   └── charts/
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
├── README.md
└── requirements.txt
```

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly
* SQLAlchemy
* SQLite
* Requests
* Jupyter Notebook
* Git & GitHub

---

## Current Status

✅ Day 1 Completed – Data Ingestion & Validation

✅ Day 2 Completed – Data Cleaning & Database Design

✅ Day 3 Completed – Exploratory Data Analysis

🔄 Day 4 – Performance Analytics & Risk Metrics

⏳ Day 5 – Dashboard Development

⏳ Day 6 – Final Reporting & Documentation

---

## Achievements

* Data ingestion pipeline implemented
* AMFI validation completed
* Live NAV integration completed
* Data cleaning pipeline created
* SQLite database designed and populated
* Analytical SQL queries implemented
* Exploratory Data Analysis completed
* Business insights generated
* Visualization framework established
* Analytics-ready datasets prepared

---

## Next Steps

* Return and risk analysis
* CAGR and rolling returns
* Volatility and drawdown analysis
* Sharpe Ratio comparison
* Benchmark comparison metrics
* Dashboard development
* KPI monitoring and reporting
