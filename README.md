# Mutual Fund Analytics – Capstone Project

## Overview

Mutual Fund Analytics is an end-to-end Data Engineering and Analytics project designed to analyze mutual fund performance, investor behavior, portfolio concentration, and risk metrics. The project covers the complete analytics pipeline, including data ingestion, validation, cleaning, exploratory data analysis, financial analytics, dashboard creation, and a rule-based recommendation engine.

---

## Objectives

* Analyze mutual fund performance and risk.
* Evaluate risk-adjusted returns.
* Study investor behavior and investment patterns.
* Measure downside risk using VaR and CVaR.
* Analyze SIP continuity and investor retention.
* Understand portfolio concentration using HHI.
* Build a mutual fund recommendation engine.
* Create interactive dashboards for business insights.

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
* Git
* GitHub
* VS Code

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
├── powerbi
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
│   ├── var_cvar_report.csv
│   ├── Final_Report.pdf
│   └── Bluestock_MF_Presentation.pptx
│
├── scripts
│   ├── amfi_validation.py
│   ├── create_db.py
│   ├── data_ingestion.py
│   ├── day2_cleaning.py
│   ├── live_nav_fetch.py
│   ├── load_data.py
│   ├── recommender.py
│   ├── run_pipeline.py
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
Financial Analytics
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
* Portfolio Concentration

## Recommendation System

* Risk-based mutual fund recommendations
* Sharpe ratio-based ranking

---

# Database Design

### Dimension Table

* dim_fund

### Fact Tables

* fact_nav
* fact_transactions
* fact_performance

SQLite was used as the analytical database for storing cleaned and transformed datasets.

---

# Power BI Dashboard

Five dashboard pages were created:

### 1. Executive Overview Dashboard

Contains:

* KPI cards
* Average ratings
* Expense ratio metrics
* Summary statistics

### 2. Fund Performance Dashboard

Contains:

* Top-performing funds
* Category comparison
* Fund house analysis

### 3. Investor Behaviour Dashboard

Contains:

* Transaction patterns
* SIP analysis
* Investor insights

### 4. Portfolio Dashboard

Contains:

* Portfolio concentration analysis
* Diversification metrics

### 5. Recommendation Dashboard

Contains:

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
* data_quality_summary.txt

---

# Scripts

| Script             | Purpose                           |
| ------------------ | --------------------------------- |
| data_ingestion.py  | Dataset inspection                |
| amfi_validation.py | AMFI code validation              |
| day2_cleaning.py   | Data cleaning                     |
| create_db.py       | Database creation                 |
| load_data.py       | Load data into SQLite             |
| verify_db.py       | Database verification             |
| live_nav_fetch.py  | Live NAV retrieval                |
| recommender.py     | Mutual fund recommendation engine |
| run_pipeline.py    | Master pipeline execution         |

---

# Running the Project

Clone the repository:

```bash
git clone <repository-url>
cd MutualFundAnalytics
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Execute the pipeline:

```bash
python scripts/run_pipeline.py
```

---

# Key Insights

* Equity funds dominate the market.
* Expense ratio significantly impacts returns.
* High-rated funds demonstrate better consistency.
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

✅ Day 1 – Project Setup

✅ Day 2 – Data Validation and Cleaning

✅ Day 3 – Exploratory Data Analysis

✅ Day 4 – Performance Analytics

✅ Day 5 – Dashboard Preparation

✅ Day 6 – Advanced Analytics

✅ Day 7 – Power BI Dashboard and Project Finalization

---

## License

This project is intended for educational purposes and portfolio demonstration.
