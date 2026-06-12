# Mutual Fund Analytics – Capstone Project

An end-to-end Data Engineering and Analytics project focused on mutual fund performance, risk analytics, investor behavior, portfolio concentration, and recommendation systems.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![SQLite](https://img.shields.io/badge/Database-SQLite-green)
![Power BI](https://img.shields.io/badge/Visualization-Power%20BI-yellow)

**GitHub Repository:** https://github.com/prs-24/MutualFundAnalytics

## Overview

Mutual Fund Analytics is an end-to-end Data Engineering and Analytics project focused on analyzing mutual fund performance, investor behavior, portfolio concentration, and risk metrics. The project covers the complete analytics lifecycle, including data ingestion, validation, cleaning, exploratory data analysis, financial analytics, database design, dashboard creation, and a rule-based recommendation engine.

---

## Objectives

* Analyze mutual fund performance and risk characteristics.
* Evaluate risk-adjusted returns using financial metrics.
* Study investor behavior and SIP continuity patterns.
* Measure downside risk using VaR and CVaR.
* Analyze portfolio concentration using HHI.
* Build a mutual fund recommendation engine.
* Develop interactive Power BI dashboards for business insights.

---

## Tech Stack

### Programming & Analytics

* Python
* Pandas
* NumPy
* Matplotlib
* SQLite
* SQL

### Visualization

* Power BI

### Development Tools

* Jupyter Notebook
* VS Code
* Git
* GitHub

---

# Project Structure

```text
MutualFundAnalytics
│
├── dashboard
│
├── data
│   ├── raw
│   └── processed
│
├── database
│   └── bluestock_mf.db
│
├── sql
│   ├── schema.sql
│   └── queries.sql
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
│   ├── fund_scorecard.csv
│   ├── hhi_concentration_report.csv
│   ├── sip_continuity_report.csv
│   ├── var_cvar_report.csv
│   ├── data_quality_summary.txt
│   ├── Final_Report.pdf
│   └── Mutual_Fund_Analytics_Presentation.pptx
│
├── scripts
│   ├── amfi_validation.py
│   ├── create_db.py
│   ├── data_ingestion.py
│   ├── day2_cleaning.py
│   ├── etl_pipeline.py
│   ├── live_nav_fetch.py
│   ├── load_data.py
│   ├── recommender.py
│   └── verify_db.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# Pipeline Architecture

```text
Raw Data
    ↓
Data Ingestion
    ↓
Data Validation
    ↓
Data Cleaning
    ↓
Exploratory Data Analysis
    ↓
Performance Analytics
    ↓
SQLite Database
    ↓
Power BI Dashboard
    ↓
Recommendation Engine
```

---

# Key Analytics Performed

## Performance Analytics

* CAGR
* Alpha
* Beta
* Sharpe Ratio
* Sortino Ratio
* Maximum Drawdown

## Risk Analytics

* Value at Risk (VaR)
* Conditional Value at Risk (CVaR)
* Rolling Sharpe Ratio

## Investor Analytics

* Investor Cohort Analysis
* SIP Continuity Analysis

## Portfolio Analytics

* Herfindahl-Hirschman Index (HHI)
* Portfolio Concentration Analysis

## Recommendation System

* Risk-based fund recommendations
* Sharpe ratio-based ranking

---

# Database Design

### Dimension Table

* dim_fund

### Fact Tables

* fact_nav
* fact_transactions
* fact_performance

SQLite is used as the analytical database for storing cleaned and transformed datasets.

---

# Power BI Dashboard

Five dashboard pages were created:

### Executive Overview Dashboard

* KPI cards
* Average ratings
* Expense ratio metrics
* Summary statistics

### Fund Performance Dashboard

* Top-performing funds
* Category comparison
* Fund house analysis

### Investor Behaviour Dashboard

* Transaction patterns
* SIP analysis
* Investor insights

### Portfolio Dashboard

* Diversification metrics
* Portfolio concentration analysis

### Recommendation Dashboard

* Risk-based filtering
* Fund recommendations

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

---

# Scripts

| Script             | Purpose                           |
| ------------------ | --------------------------------- |
| data_ingestion.py  | Dataset ingestion                 |
| amfi_validation.py | AMFI code validation              |
| day2_cleaning.py   | Data cleaning                     |
| create_db.py       | Database creation                 |
| load_data.py       | Load data into SQLite             |
| verify_db.py       | Database verification             |
| live_nav_fetch.py  | Live NAV retrieval                |
| recommender.py     | Mutual fund recommendation engine |
| etl_pipeline.py    | Master ETL pipeline               |

---

# Running the Project

Clone the repository:

```bash
git clone https://github.com/prs-24/MutualFundAnalytics.git
cd MutualFundAnalytics
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Execute the ETL pipeline:

```bash
python scripts/etl_pipeline.py
```

---

# Key Insights

* Equity funds dominate the mutual fund market.
* Expense ratio has a significant impact on returns.
* Highly rated funds demonstrate better consistency.
* SIP continuity varies across investors.
* Portfolio concentration differs among schemes.
* Risk-adjusted metrics provide deeper insights than absolute returns.

---

# Future Enhancements

* Machine Learning-based recommendation engine.
* Streamlit web application.
* Real-time API integration.
* Predictive analytics and forecasting.
* Portfolio optimization models.

---

# Project Status

✅ Project Setup and Data Collection

✅ Data Validation and Cleaning

✅ Exploratory Data Analysis

✅ Performance Analytics

✅ Dashboard Development

✅ Advanced Analytics

✅ Recommendation Engine

✅ Project Finalization

---

## License

This project is intended for educational purposes and portfolio demonstration.
