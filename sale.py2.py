# Import Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset

df = pd.read_csv("sales_data.csv")

# ----------------------------
# DATA CLEANING
# ----------------------------

# Remove duplicates
df.drop_duplicates(inplace=True)

# Handle missing values
df.fillna(0, inplace=True)

# Convert date column
df['Order_Date'] = pd.to_datetime(df['Order_Date'])

# Check data
print(df.info())

# ----------------------------
# KPI CALCULATIONS
# ----------------------------

total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
total_orders = df['Order_ID'].nunique()

print("Total Sales:", total_sales)
print("Total Profit:", total_profit)
print("Total Orders:", total_orders)

# ----------------------------
# SALES BY REGION
# ----------------------------

region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(8,5))
sns.barplot(x=region_sales.index,
            y=region_sales.values,
            palette='viridis')

plt.title('Sales by Region')
plt.xlabel('Region')
plt.ylabel('Sales')
plt.show()

# ----------------------------
# CATEGORY PERFORMANCE
# ----------------------------

category_profit = df.groupby('Category')['Profit'].sum()

plt.figure(figsize=(8,5))
category_profit.plot(kind='bar', color='orange')

plt.title('Profit by Category')
plt.ylabel('Profit')
plt.show()

# ----------------------------
# MONTHLY SALES TREND
# ----------------------------

df['Month'] = df['Order_Date'].dt.to_period('M')

monthly_sales = df.groupby('Month')['Sales'].sum()

plt.figure(figsize=(12,5))
monthly_sales.plot()

plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
plt.show()

# ----------------------------
# TOP CUSTOMERS
# ----------------------------

top_customers = (
    df.groupby('Customer_ID')['Sales']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Customers")
print(top_customers)

# ----------------------------
# BUSINESS INSIGHTS
# ----------------------------

best_region = region_sales.idxmax()
best_category = category_profit.idxmax()

print(f"\nHighest Sales Region: {best_region}")
print(f"Most Profitable Category: {best_category}")
