import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.float_format = "{:,.2f}".format

df = pd.read_csv("Cleaned_Walmart.csv")


# Top 10 Stores by Sales
top10 = (
    df.groupby("Store")["Weekly_Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(10,6))
plt.bar(top10.index.astype(str), top10.values)

plt.title("Top 10 Stores by Total Sales")
plt.xlabel("Store")
plt.ylabel("Sales ($)")

plt.tight_layout()
plt.show()

# Bottom 10 Stores
bottom10 = (
    df.groupby("Store")["Weekly_Sales"]
      .sum()
      .sort_values()
      .head(10)
)

plt.figure(figsize=(10,6))
plt.bar(bottom10.index.astype(str), bottom10.values)

plt.title("Bottom 10 Stores by Total Sales")
plt.xlabel("Store")
plt.ylabel("Sales ($)")

plt.tight_layout()
plt.show()

# Monthly Sales Trend
monthly = (
    df.groupby(["Month_Number","Month"])["Weekly_Sales"]
      .sum()
      .reset_index()
      .sort_values("Month_Number")
)

plt.figure(figsize=(12,6))

plt.plot(
    monthly["Month"],
    monthly["Weekly_Sales"],
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales ($)")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# Quarterly Sales
quarter = (
    df.groupby("Quarter")["Weekly_Sales"]
      .sum()
)

plt.figure(figsize=(7,5))

plt.bar(quarter.index, quarter.values)

plt.title("Quarterly Sales")

plt.xlabel("Quarter")

plt.ylabel("Sales ($)")

plt.tight_layout()

plt.show()


# Holiday vs Non-Holiday
holiday = (
    df.groupby("Holiday_Flag")["Weekly_Sales"]
      .mean()
)

plt.figure(figsize=(6,5))

plt.bar(holiday.index, holiday.values)

plt.title("Average Weekly Sales")

plt.xlabel("Holiday")

plt.ylabel("Average Sales ($)")

plt.tight_layout()

plt.show()


# Sales Distribution
plt.figure(figsize=(8,5))

plt.hist(df["Weekly_Sales"], bins=25)

plt.title("Distribution of Weekly Sales")

plt.xlabel("Weekly Sales")

plt.ylabel("Frequency")

plt.tight_layout()

plt.show()


# Temperature vs Sales
plt.figure(figsize=(8,6))

plt.scatter(
    df["Temperature"],
    df["Weekly_Sales"]
)

plt.title("Temperature vs Weekly Sales")

plt.xlabel("Temperature")

plt.ylabel("Weekly Sales")

plt.tight_layout()

plt.show()


# Fuel Price vs Sales
plt.figure(figsize=(8,6))

plt.scatter(
    df["Fuel_Price"],
    df["Weekly_Sales"]
)

plt.title("Fuel Price vs Weekly Sales")

plt.xlabel("Fuel Price")

plt.ylabel("Weekly Sales")

plt.tight_layout()

plt.show()


# CPI vs Sales
plt.figure(figsize=(8,6))

plt.scatter(
    df["CPI"],
    df["Weekly_Sales"]
)

plt.title("CPI vs Weekly Sales")

plt.xlabel("CPI")

plt.ylabel("Weekly Sales")

plt.tight_layout()

plt.show()



# Unemployment vs Sales
plt.figure(figsize=(8,6))

plt.scatter(
    df["Unemployment"],
    df["Weekly_Sales"]
)

plt.title("Unemployment vs Weekly Sales")

plt.xlabel("Unemployment")

plt.ylabel("Weekly Sales")

plt.tight_layout()

plt.show()