# Mutual Fund Analytics – Capstone Project

## Overview

Mutual Fund Analytics is a data engineering and analytics project designed to analyze mutual fund performance, investor behavior, AUM trends, SIP inflows, portfolio holdings, and benchmark indices.

The project focuses on building a complete analytics pipeline, starting from raw data ingestion and validation to data cleaning, database design, and analytical SQL reporting.

---

## Project Objectives

* Collect and validate mutual fund datasets
* Perform data quality assessment and cleaning
* Standardize and validate financial data
* Design a structured SQLite analytics database
* Generate business insights using SQL queries
* Create reusable data pipelines for future dashboarding and reporting

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

## Objectives

### Data Cleaning

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

Designed and implemented a SQLite analytics database.

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

Implemented 10 analytical SQL queries including:

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
├── scripts/
│   ├── data_ingestion.py
│   ├── amfi_validation.py
│   ├── live_nav_fetch.py
│   ├── day2_cleaning.py
│   ├── create_db.py
│   ├── load_data.py
│   └── verify_db.py
│
├── reports/
│
├── README.md
└── requirements.txt
```

---

## Technologies Used

* Python
* Pandas
* NumPy
* SQLAlchemy
* SQLite
* Requests
* Git & GitHub

---

## Current Status

✅ Day 1 Completed

✅ Day 2 Completed

### Achievements

* Data ingestion pipeline implemented
* Data validation completed
* Live NAV integration completed
* Data cleaning pipeline created
* SQLite database designed and populated
* Analytical SQL queries implemented
* Data dictionary documented

---

## Next Steps

* Dashboard development
* Advanced analytics
* Data visualization
* KPI tracking
* Investor insights reporting
* Mutual fund performance monitoring
