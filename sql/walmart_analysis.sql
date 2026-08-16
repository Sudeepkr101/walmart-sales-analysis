-- Create and select the Walmart analysis database
CREATE DATABASE walmart_analysis;
USE walmart_analysis;


-- Preview the first 10 rows
SELECT *
FROM cleaned_walmart
LIMIT 10;


-- Count total number of rows
SELECT COUNT(*) AS Total_Rows
FROM cleaned_walmart;


-- Count total number of unique stores
SELECT COUNT(DISTINCT Store) AS Number_of_Stores
FROM cleaned_walmart;


-- Find the dataset date range
SELECT
    MIN(Date) AS Start_Date,
    MAX(Date) AS End_Date
FROM cleaned_walmart;


-- Check missing values in important columns
SELECT
    COUNT(*) AS Total_Rows,
    COUNT(Store) AS Store_Values,
    COUNT(Date) AS Date_Values,
    COUNT(Weekly_Sales) AS Sales_Values,
    COUNT(Temperature) AS Temperature_Values,
    COUNT(Fuel_Price) AS Fuel_Values,
    COUNT(CPI) AS CPI_Values,
    COUNT(Unemployment) AS Unemployment_Values
FROM cleaned_walmart;


-- Count rows for holiday and non-holiday weeks
SELECT
    Holiday_Flag,
    COUNT(*) AS Number_of_Rows
FROM cleaned_walmart
GROUP BY Holiday_Flag;


-- Check for duplicate Store-Date records
SELECT
    Store,
    Date,
    COUNT(*) AS Duplicate_Count
FROM cleaned_walmart
GROUP BY Store, Date
HAVING COUNT(*) > 1;


-- Find records with invalid or zero sales
SELECT *
FROM cleaned_walmart
WHERE Weekly_Sales <= 0;


-- Find invalid temperature values
SELECT *
FROM cleaned_walmart
WHERE Temperature IS NULL
   OR Temperature < -100
   OR Temperature > 150;


-- Calculate overall sales statistics
SELECT
    MIN(Weekly_Sales) AS Minimum_Sales,
    MAX(Weekly_Sales) AS Maximum_Sales,
    AVG(Weekly_Sales) AS Average_Sales,
    SUM(Weekly_Sales) AS Total_Sales
FROM cleaned_walmart;


-- Calculate total sales by store
SELECT
    Store,
    SUM(Weekly_Sales) AS Total_Sales
FROM cleaned_walmart
GROUP BY Store
ORDER BY Total_Sales DESC;


-- Find the top 10 stores by total sales
SELECT
    Store,
    SUM(Weekly_Sales) AS Total_Sales
FROM cleaned_walmart
GROUP BY Store
ORDER BY Total_Sales DESC
LIMIT 10;


-- Find the bottom 10 stores by total sales
SELECT
    Store,
    SUM(Weekly_Sales) AS Total_Sales
FROM cleaned_walmart
GROUP BY Store
ORDER BY Total_Sales ASC
LIMIT 10;


-- Find stores with the highest average weekly sales
SELECT
    Store,
    AVG(Weekly_Sales) AS Average_Weekly_Sales
FROM cleaned_walmart
GROUP BY Store
ORDER BY Average_Weekly_Sales DESC;


-- Calculate total sales by year
SELECT
    Year,
    SUM(Weekly_Sales) AS Total_Sales
FROM cleaned_walmart
GROUP BY Year
ORDER BY Year;


-- Calculate total sales by month across all years
SELECT
    Month_Number,
    Month,
    SUM(Weekly_Sales) AS Total_Sales
FROM cleaned_walmart
GROUP BY Month_Number, Month
ORDER BY Month_Number;


-- Calculate total sales by quarter across all years
SELECT
    Quarter,
    SUM(Weekly_Sales) AS Total_Sales
FROM cleaned_walmart
GROUP BY Quarter
ORDER BY Quarter;


-- Calculate total sales by year and quarter
SELECT
    Year,
    Quarter,
    SUM(Weekly_Sales) AS Total_Sales
FROM cleaned_walmart
GROUP BY Year, Quarter
ORDER BY Year, Quarter;


-- Compare average and total sales on holidays vs non-holidays
SELECT
    Holiday_Flag,
    AVG(Weekly_Sales) AS Average_Sales,
    SUM(Weekly_Sales) AS Total_Sales
FROM cleaned_walmart
GROUP BY Holiday_Flag;


-- Find the top 10 highest weekly sales records
SELECT
    Store,
    Date,
    Weekly_Sales
FROM cleaned_walmart
ORDER BY Weekly_Sales DESC
LIMIT 10;


-- Find the 10 lowest weekly sales records
SELECT
    Store,
    Date,
    Weekly_Sales
FROM cleaned_walmart
ORDER BY Weekly_Sales ASC
LIMIT 10;


-- Rank stores by total sales
SELECT
    Store,
    SUM(Weekly_Sales) AS Total_Sales,
    RANK() OVER (
        ORDER BY SUM(Weekly_Sales) DESC
    ) AS Sales_Rank
FROM cleaned_walmart
GROUP BY Store
ORDER BY Sales_Rank;


-- Compare store sales performance across years
SELECT
    Year,
    Store,
    SUM(Weekly_Sales) AS Total_Sales
FROM cleaned_walmart
GROUP BY Year, Store
ORDER BY Year, Total_Sales DESC;


-- Compare average sales across weekdays
SELECT
    Day,
    AVG(Weekly_Sales) AS Average_Sales
FROM cleaned_walmart
GROUP BY Day
ORDER BY AVG(Weekly_Sales) DESC;


-- Analyze average sales at different fuel prices
SELECT
    ROUND(Fuel_Price, 2) AS Fuel_Price,
    AVG(Weekly_Sales) AS Average_Sales
FROM cleaned_walmart
GROUP BY ROUND(Fuel_Price, 2)
ORDER BY Fuel_Price;


-- Analyze average sales at different unemployment rates
SELECT
    ROUND(Unemployment, 1) AS Unemployment_Rate,
    AVG(Weekly_Sales) AS Average_Sales
FROM cleaned_walmart
GROUP BY ROUND(Unemployment, 1)
ORDER BY Unemployment_Rate;


-- Create a reusable store sales summary view
CREATE VIEW store_sales_summary AS
SELECT
    Store,
    SUM(Weekly_Sales) AS Total_Sales,
    AVG(Weekly_Sales) AS Average_Weekly_Sales,
    MIN(Weekly_Sales) AS Minimum_Weekly_Sales,
    MAX(Weekly_Sales) AS Maximum_Weekly_Sales
FROM cleaned_walmart
GROUP BY Store;


-- Display stores using the sales summary view
SELECT *
FROM store_sales_summary
ORDER BY Total_Sales DESC;



-- Advance buisness analysis

-- Store Sales ranking
SELECT
    Store,
    SUM(Weekly_Sales) AS Total_Sales,
    RANK() OVER (
        ORDER BY SUM(Weekly_Sales) DESC
    ) AS Sales_Rank
FROM cleaned_walmart
GROUP BY Store

-- Store performance by year
SELECT
    Year,
    Store,
    SUM(Weekly_Sales) AS Total_Sales
FROM cleaned_walmart
GROUP BY Year, Store
ORDER BY Year, Total_Sales DESC;

-- year over year sales
WITH yearly_sales AS (
    SELECT
        Year,
        SUM(Weekly_Sales) AS Total_Sales
    FROM cleaned_walmart
    GROUP BY Year
)

SELECT
    Year,
    Total_Sales,
    LAG(Total_Sales) OVER (ORDER BY Year) AS Previous_Year_Sales,
    Total_Sales -
        LAG(Total_Sales) OVER (ORDER BY Year) AS Sales_Change
FROM yearly_sales
ORDER BY Year;

-- year over year percentage change
WITH yearly_sales AS (
    SELECT
        Year,
        SUM(Weekly_Sales) AS Total_Sales
    FROM cleaned_walmart
    GROUP BY Year
)

SELECT
    Year,
    Total_Sales,
    LAG(Total_Sales) OVER (ORDER BY Year) AS Previous_Year_Sales,

    ROUND(
        (
            Total_Sales -
            LAG(Total_Sales) OVER (ORDER BY Year)
        )
        /
        LAG(Total_Sales) OVER (ORDER BY Year)
        * 100,
        2
    ) AS YoY_Growth_Percent

FROM yearly_sales
ORDER BY Year;

-- best month
SELECT
    Month_Number,
    Month,
    SUM(Weekly_Sales) AS Total_Sales
FROM cleaned_walmart
GROUP BY Month_Number, Month
ORDER BY Total_Sales DESC;

-- Best quarter
SELECT
    Quarter,
    SUM(Weekly_Sales) AS Total_Sales
FROM cleaned_walmart
GROUP BY Quarter
ORDER BY Total_Sales DESC;

-- holiday impact
SELECT
    AVG(CASE
        WHEN Holiday_Flag = 'Yes'
        THEN Weekly_Sales
    END) AS Holiday_Avg_Sales,

    AVG(CASE
        WHEN Holiday_Flag = 'No'
        THEN Weekly_Sales
    END) AS Non_Holiday_Avg_Sales,

-- difference
    AVG(CASE
        WHEN Holiday_Flag = 'Yes'
        THEN Weekly_Sales
    END)
    -
    AVG(CASE
        WHEN Holiday_Flag = 'NO'
        THEN Weekly_Sales
    END) AS Difference

FROM cleaned_walmart;


-- each store's highest-selling week
WITH ranked_sales AS (
    SELECT
        Store,
        Date,
        Weekly_Sales,
        RANK() OVER (
            PARTITION BY Store
            ORDER BY Weekly_Sales DESC
        ) AS Sales_Rank
    FROM cleaned_walmart
)

SELECT
    Store,
    Date,
    Weekly_Sales
FROM ranked_sales
WHERE Sales_Rank = 1
ORDER BY Store;


-- Top 5 stores by average weekly sales
SELECT
    Store,
    ROUND(AVG(Weekly_Sales), 2) AS Average_Weekly_Sales
FROM cleaned_walmart
GROUP BY Store
ORDER BY Average_Weekly_Sales DESC
LIMIT 5;

-- Store contribution to total sales
SELECT
    Store,
    SUM(Weekly_Sales) AS Store_Sales,

    ROUND(
        SUM(Weekly_Sales)
        /
        (SELECT SUM(Weekly_Sales)
         FROM cleaned_walmart)
        * 100,
        2
    ) AS Sales_Contribution_Percent

FROM cleaned_walmart
GROUP BY Store
ORDER BY Store_Sales DESC;