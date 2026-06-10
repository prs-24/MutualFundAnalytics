# Mutual Fund Analytics – Capstone Project

## Overview

Mutual Fund Analytics is an end-to-end data analytics project aimed at analyzing mutual fund performance, investor behavior, portfolio concentration, and risk metrics. The project covers the complete analytics pipeline from data ingestion and validation to advanced financial analytics and dashboard-ready outputs.

---

## Objectives

* Analyze mutual fund performance and risk.
* Evaluate risk-adjusted returns.
* Study investor behavior and investment patterns.
* Measure downside risk using VaR and CVaR.
* Analyze SIP continuity and investor retention.
* Understand portfolio concentration using HHI.
* Build a simple fund recommendation engine.
* Prepare data for dashboarding and business insights.

---

## Tech Stack

* Python
* Pandas
* NumPy
* Matplotlib
* SQLite
* SQL
* Jupyter Notebook
* Git & GitHub
* Power BI (Day 7)

---

# Project Structure

```text
MutualFundAnalytics
│
├── .venv
├── dashboard
│
├── data
│   ├── raw
│   └── processed
│
├── database
│   ├── bluestock_mf.db
│   ├── queries.sql
│   └── schema.sql
│
├── docs
│   └── data_dictionary.md
│
├── notebooks
│   ├── EDA_Analysis.ipynb
│   ├── performance_analytics.ipynb
│   └── Advance_Analytics.ipynb
│
├── reports
│   ├── charts
│   ├── alpha_beta.csv
│   ├── cagr_results.csv
│   ├── cohort_summary.csv
│   ├── cohort_top_funds.csv
│   ├── data_quality_summary.txt
│   ├── fund_scorecard.csv
│   ├── hhi_concentration_report.csv
│   ├── sip_continuity_report.csv
│   └── var_cvar_report.csv
│
├── scripts
│   ├── amfi_validation.py
│   ├── create_db.py
│   ├── data_ingestion.py
│   ├── day2_cleaning.py
│   ├── live_nav_fetch.py
│   ├── load_data.py
│   ├── recommender.py
│   └── verify_db.py
│
├── sql
├── requirements.txt
├── .gitignore
└── README.md
```

---

# Day-wise Progress

## Day 1 – Project Setup and Data Collection

* Repository initialization
* Folder structure setup
* Virtual environment creation
* Dataset collection
* GitHub integration

---

## Day 2 – Data Validation and Cleaning

Performed:

* Missing value analysis
* Duplicate checks
* Data type corrections
* Data cleaning and preprocessing

Generated:

* Cleaned datasets
* Data quality summary report

Scripts:

* `day2_cleaning.py`
* `amfi_validation.py`

---

## Day 3 – Exploratory Data Analysis

Performed:

* Fund category analysis
* Fund house analysis
* Investor demographics analysis
* Transaction analysis
* Descriptive statistics

Notebook:

* `EDA_Analysis.ipynb`

---

## Day 4 – Performance Analytics

Calculated:

* CAGR
* Alpha
* Beta
* Sharpe Ratio
* Sortino Ratio
* Maximum Drawdown

Generated:

* `alpha_beta.csv`
* `cagr_results.csv`
* `fund_scorecard.csv`

Notebook:

* `performance_analytics.ipynb`

---

## Day 5 – Dashboard Data Preparation

Prepared analytical outputs for:

* Fund performance dashboard
* Investor insights
* Risk analysis
* Portfolio analysis

Generated dashboard-ready datasets.

---

## Day 6 – Advanced Analytics and Risk Metrics

### Historical Risk Analysis

Computed:

* Value at Risk (VaR 95%)
* Conditional Value at Risk (CVaR 95%)

Generated:

* `var_cvar_report.csv`

---

### Rolling Sharpe Ratio

Computed:

* 90-Day Rolling Sharpe Ratio

Generated:

* `reports/charts/rolling_sharpe_chart.png`

---

### Investor Cohort Analysis

Analyzed:

* Investor cohorts based on first transaction year
* Average investment amount
* Total investment
* Top fund preferences

Generated:

* `cohort_summary.csv`
* `cohort_top_funds.csv`

---

### SIP Continuity Analysis

Analyzed:

* Average gap between transactions
* Investor continuity

Generated:

* `sip_continuity_report.csv`

Observation:

* Healthy Investors: 188
* At-Risk Investors: 2762

---

### Portfolio Concentration Analysis

Computed:

* Herfindahl-Hirschman Index (HHI)

Generated:

* `hhi_concentration_report.csv`

---

### Recommendation System

Implemented:

* Risk-based mutual fund recommendation engine

Script:

* `recommender.py`

---

# Reports Generated

* alpha_beta.csv
* cagr_results.csv
* cohort_summary.csv
* cohort_top_funds.csv
* fund_scorecard.csv
* hhi_concentration_report.csv
* sip_continuity_report.csv
* var_cvar_report.csv
* data_quality_summary.txt

---

# Key Techniques Used

* CAGR
* Alpha and Beta Analysis
* Sharpe Ratio
* Sortino Ratio
* Maximum Drawdown
* Value at Risk (VaR)
* Conditional Value at Risk (CVaR)
* Rolling Sharpe Ratio
* Investor Cohort Analysis
* SIP Continuity Analysis
* Herfindahl-Hirschman Index (HHI)
* Recommendation System

---

# Current Status

✅ Day 1 Completed

✅ Day 2 Completed

✅ Day 3 Completed

✅ Day 4 Completed

✅ Day 5 Completed

✅ Day 6 Completed

---

## Next Phase

### Day 7

* Power BI Dashboard
* Business Storytelling
* Final Documentation
* GitHub Project Finalization

---


## License

This project is intended for educational and portfolio purposes.
