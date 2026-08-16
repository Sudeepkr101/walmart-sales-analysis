import pandas as pd
import numpy as np

df = pd.read_csv("Walmart.csv")

# print(df.dtypes)
# df.info()
# print(df.isnull().sum())
# print("Duplicate Rows:", df.duplicated().sum())
# print(df["Store"].duplicated().sum())
# print(df.dtypes)

df["Date"] = pd.to_datetime(
    df["Date"],
    format="mixed",
    dayfirst=True
)

# print(df.dtypes)

# print(df.head())

# print(df.describe())

# print(df[df["Weekly_Sales"] < 0])
# print(df[df["Fuel_Price"] < 0])
# print(df[df["Temperature"] < -100])
# print(df[df["Unemployment"] < 0])


df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month_name()
df["Month_Number"] = df["Date"].dt.month
df["Quarter"] = "Q" + df["Date"].dt.quarter.astype(str)
df["Week"] = df["Date"].dt.isocalendar().week
df["Day"] = df["Date"].dt.day
# print(df.head())

df["Holiday_Flag"] = df["Holiday_Flag"].map({
    0: "No",
    1: "Yes"
})
print(df.head())

# print(df.dtypes)

df.to_csv("Cleaned_Walmart.csv", index=False)

print("Cleaned dataset saved successfully!")
