# =====================================================
# Walmart Sales Analytics Project
# Exploratory Data Analysis (EDA)
# Author: Sudeep Kumar
# =====================================================

# ==========================
# IMPORT LIBRARIES
# ==========================

import csv
import os

import pandas as pd

# Display numbers in readable format
pd.options.display.float_format = "{:,.2f}".format

# ==========================
# LOAD DATASET
# ==========================

df = pd.read_csv("Cleaned_Walmart.csv")

# ==========================
# DATASET INFORMATION
# ==========================

print("=" * 60)
print("DATASET INFORMATION")
print("=" * 60)

df.info()

print("\nDataset Shape :", df.shape)
print("Number of Stores :", df["Store"].nunique())

# ==========================
# DESCRIPTIVE STATISTICS
# ==========================

print("\n" + "=" * 60)
print("DATASET SUMMARY")
print("=" * 60)

print(df.describe())

# ==========================
# SALES BY STORE
# ==========================

store_sales = (
    df.groupby("Store")["Weekly_Sales"]
      .sum()
      .sort_values(ascending=False)
)

print("\n" + "=" * 60)
print("TOTAL SALES BY STORE")
print("=" * 60)

print(store_sales)

# ==========================
# TOP 10 STORES
# ==========================

print("\n" + "=" * 60)
print("TOP 10 STORES")
print("=" * 60)

print(store_sales.head(10))

# ==========================
# BOTTOM 10 STORES
# ==========================

print("\n" + "=" * 60)
print("BOTTOM 10 STORES")
print("=" * 60)

print(store_sales.tail(10))

# ==========================
# HOLIDAY SALES
# ==========================

holiday_sales = (
    df.groupby("Holiday_Flag")["Weekly_Sales"]
      .mean()
)

print("\n" + "=" * 60)
print("AVERAGE SALES : HOLIDAY VS NON-HOLIDAY")
print("=" * 60)

print(holiday_sales)

# ==========================
# MONTHLY SALES
# ==========================

monthly_sales = (
    df.groupby(["Month_Number", "Month"])["Weekly_Sales"]
      .sum()
      .reset_index()
      .sort_values("Month_Number")
)

print("\n" + "=" * 60)
print("MONTHLY SALES")
print("=" * 60)

print(monthly_sales)

# ==========================
# QUARTERLY SALES
# ==========================

quarter_sales = (
    df.groupby("Quarter")["Weekly_Sales"]
      .sum()
)

print("\n" + "=" * 60)
print("QUARTERLY SALES")
print("=" * 60)

print(quarter_sales)

# ==========================
# YEARLY SALES
# ==========================

yearly_sales = (
    df.groupby("Year")["Weekly_Sales"]
      .sum()
)

print("\n" + "=" * 60)
print("YEARLY SALES")
print("=" * 60)

print(yearly_sales)

# ==========================
# HIGHEST & LOWEST SALES
# ==========================

print("\n" + "=" * 60)
print("HIGHEST WEEKLY SALES RECORD")
print("=" * 60)

print(df.loc[df["Weekly_Sales"].idxmax()])

print("\n" + "=" * 60)
print("LOWEST WEEKLY SALES RECORD")
print("=" * 60)

print(df.loc[df["Weekly_Sales"].idxmin()])

# ==========================
# CORRELATION ANALYSIS
# ==========================

corr = df[
    [
        "Weekly_Sales",
        "Temperature",
        "Fuel_Price",
        "CPI",
        "Unemployment",
    ]
].corr()

print("\n" + "=" * 60)
print("CORRELATION MATRIX")
print("=" * 60)

print(corr)

# ==========================
# SAVE EDA RESULTS TO CSV
# ==========================

# Create output directory
output_dir = "eda_results"
os.makedirs(output_dir, exist_ok=True)

# Dataset summary
df.describe().to_csv(os.path.join(output_dir, "dataset_summary.csv"))

# Store sales (total)
store_sales_df = store_sales.reset_index()
store_sales_df.columns = ["Store", "Total_Sales"]
store_sales_df.to_csv(os.path.join(output_dir, "store_sales_total.csv"), index=False)

# Top 10 and bottom 10 stores
store_sales.head(10).reset_index().rename(columns={"Store": "Store", "Weekly_Sales": "Total_Sales"}).to_csv(
    os.path.join(output_dir, "top_10_stores.csv"), index=False
)
store_sales.tail(10).reset_index().rename(columns={"Store": "Store", "Weekly_Sales": "Total_Sales"}).to_csv(
    os.path.join(output_dir, "bottom_10_stores.csv"), index=False
)

# Holiday sales (average)
holiday_sales_df = holiday_sales.reset_index()
holiday_sales_df.columns = ["Holiday_Flag", "Average_Weekly_Sales"]
holiday_sales_df.to_csv(os.path.join(output_dir, "holiday_avg_sales.csv"), index=False)

# Monthly, quarterly, yearly sales
monthly_sales.to_csv(os.path.join(output_dir, "monthly_sales.csv"), index=False)
quarter_sales.reset_index().to_csv(os.path.join(output_dir, "quarterly_sales.csv"), index=False)
yearly_sales.reset_index().to_csv(os.path.join(output_dir, "yearly_sales.csv"), index=False)

# Highest and lowest weekly sales records
highest_record = df.loc[df["Weekly_Sales"].idxmax()].to_frame().T
lowest_record = df.loc[df["Weekly_Sales"].idxmin()].to_frame().T
highest_record["Record"] = "Highest"
lowest_record["Record"] = "Lowest"
pd.concat([highest_record, lowest_record], ignore_index=True).to_csv(
    os.path.join(output_dir, "highest_lowest_records.csv"), index=False
)

# Correlation matrix
corr.to_csv(os.path.join(output_dir, "correlation_matrix.csv"))

# Key insights (simple key-value pairs)
# compute store-level insights
highest_store = store_sales.idxmax()
lowest_store = store_sales.idxmin()

insights = {
    "Highest_Revenue_Store": f"Store {highest_store}",
    "Lowest_Revenue_Store": f"Store {lowest_store}",
    "Highest_Weekly_Sale": f"{df['Weekly_Sales'].max():.2f}",
    "Lowest_Weekly_Sale": f"{df['Weekly_Sales'].min():.2f}",
    "Average_Weekly_Sale": f"{df['Weekly_Sales'].mean():.2f}",
}
insights_df = pd.DataFrame(list(insights.items()), columns=["Metric", "Value"])
insights_df.to_csv(os.path.join(output_dir, "key_insights.csv"), index=False)

# Create a single combined CSV containing labeled sections for quick review
combined_path = os.path.join(output_dir, "combined_summary.csv")
with open(combined_path, "w", newline="", encoding="utf-8") as f:
    # Dataset summary
    f.write("SECTION,DATASET_SUMMARY\n")
    df.describe().to_csv(f)
    f.write("\n")

    # Store sales total
    f.write("SECTION,STORE_SALES_TOTAL\n")
    store_sales_df.to_csv(f, index=False)
    f.write("\n")

    # Top 10
    f.write("SECTION,TOP_10_STORES\n")
    store_sales.head(10).reset_index().rename(columns={"Store": "Store", "Weekly_Sales": "Total_Sales"}).to_csv(f, index=False)
    f.write("\n")

    # Bottom 10
    f.write("SECTION,BOTTOM_10_STORES\n")
    store_sales.tail(10).reset_index().rename(columns={"Store": "Store", "Weekly_Sales": "Total_Sales"}).to_csv(f, index=False)
    f.write("\n")

    # Holiday average
    f.write("SECTION,HOLIDAY_AVG_SALES\n")
    holiday_sales_df.to_csv(f, index=False)
    f.write("\n")

    # Monthly, quarterly, yearly
    f.write("SECTION,MONTHLY_SALES\n")
    monthly_sales.to_csv(f, index=False)
    f.write("\n")

    f.write("SECTION,QUARTERLY_SALES\n")
    quarter_sales.reset_index().to_csv(f, index=False)
    f.write("\n")

    f.write("SECTION,YEARLY_SALES\n")
    yearly_sales.reset_index().to_csv(f, index=False)
    f.write("\n")

    # Highest and lowest records
    f.write("SECTION,HIGHEST_LOWEST_RECORDS\n")
    pd.concat([highest_record, lowest_record], ignore_index=True).to_csv(f, index=False)
    f.write("\n")

    # Correlation matrix
    f.write("SECTION,CORRELATION_MATRIX\n")
    corr.to_csv(f)
    f.write("\n")

    # Key insights
    f.write("SECTION,KEY_INSIGHTS\n")
    insights_df.to_csv(f, index=False)

print(f"\nEDA results saved to directory: {output_dir}")
print(f"Combined summary written to: {combined_path}")

# ==========================
# KEY INSIGHTS
# ==========================

highest_store = store_sales.idxmax()
lowest_store = store_sales.idxmin()

print("\n" + "=" * 60)
print("KEY INSIGHTS")
print("=" * 60)

print(f"Highest Revenue Store : Store {highest_store}")
print(f"Lowest Revenue Store  : Store {lowest_store}")

print(
    f"Highest Weekly Sale : ${df['Weekly_Sales'].max():,.2f}"
)

print(
    f"Lowest Weekly Sale  : ${df['Weekly_Sales'].min():,.2f}"
)

print(
    f"Average Weekly Sale : ${df['Weekly_Sales'].mean():,.2f}"
)

if holiday_sales["Yes"] > holiday_sales["No"]:
    print("\nHoliday weeks generate higher average sales.")
else:
    print("\nNon-holiday weeks generate higher average sales.")

print("\nEDA Completed Successfully.")



