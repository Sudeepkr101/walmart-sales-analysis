# Walmart Sales Analysis

An end-to-end retail sales analytics project using **Python, SQL, and Power BI** to analyze Walmart weekly sales performance across stores, time periods, holidays, and selected external factors.

---

## 📊 Project Overview

This project analyzes Walmart's historical weekly sales data to identify:

- Store-level sales performance
- Annual, quarterly, and monthly trends
- Seasonal patterns
- Holiday vs. non-holiday sales behavior
- Relationships between sales and external factors
- High- and low-performing stores
- Business opportunities for inventory, staffing, and operational planning

The project follows an end-to-end analytics workflow:

**Python → SQL → Power BI**

---

## 🎯 Business Objectives

The analysis was designed to answer key business questions:

1. Which stores generate the highest and lowest sales?
2. How do sales change across years?
3. Which months and quarters perform best?
4. Do holiday weeks generate higher sales?
5. Are sales related to fuel prices, unemployment, or temperature?
6. Which stores require greater operational attention?
7. What seasonal patterns can support business planning?

---

## 📁 Dataset

The dataset contains Walmart weekly sales information across **45 stores**.

### Coverage

- **Period:** February 2010 – October 2012
- **Stores:** 45
- **Observations:** 6,435 weekly records

### Main Variables

| Variable | Description |
|---|---|
| Store | Store identifier |
| Date | Weekly observation date |
| Weekly_Sales | Weekly sales amount |
| Holiday_Flag | Indicates whether the week is a designated holiday week |
| Temperature | Recorded temperature |
| Fuel_Price | Fuel price |
| CPI | Consumer Price Index |
| Unemployment | Unemployment rate |

Additional time-based features such as Year, Month, Month Number, Quarter, Week, and Day were created during preprocessing.

---

## 🛠️ Tools & Technologies

### Python
- Pandas
- NumPy
- Matplotlib

Used for:
- Data cleaning
- Data type correction
- Missing-value checks
- Duplicate checks
- Feature engineering
- Exploratory data analysis

### SQL / MySQL

Used for:
- Data validation
- Aggregation
- Store performance analysis
- Time-based analysis
- Holiday analysis
- Ranking
- Year-over-year analysis
- Window functions
- Business analysis

### Power BI

Used for:
- Data modeling
- DAX measures
- KPI development
- Interactive visualizations
- Slicers and filtering
- Dashboard storytelling

---

## 📊 Power BI Dashboard

The Power BI dashboard contains three analytical pages:

### 1. Sales Analytics
This page provides a high-level overview of total sales and performance metrics.
![Sales Analytics](screenshots/Sales%20Analytics.png)

### 2. Sales Trends & Drivers
This page explores how sales fluctuate over time and are affected by external factors.
![Sales Trends & Drivers](screenshots/Sales%20Trend%20and%20drivers.png)

### 3. Store Performance
This page breaks down sales by individual stores to highlight top and bottom performers.
![Store Performance](screenshots/Store%20performance.png)

---

## 🔄 Project Workflow

```text
Raw Walmart Dataset
        ↓
Python
Data Cleaning & EDA
        ↓
Cleaned Dataset
        ↓
MySQL
Data Validation & Business Analysis
        ↓
Power BI
Interactive Dashboard
        ↓
Business Insights & Recommendations
