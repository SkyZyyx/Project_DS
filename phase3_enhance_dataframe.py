"""
Phase 3: Enhance DataFrame with calculated metrics
"""

import pandas as pd
import numpy as np

print("=" * 60)
print("Phase 3: Enhancing DataFrame")
print("=" * 60)

# Step 1: Load the data we created in Phase 2
print("\n1. Loading initial.csv...")
df = pd.read_csv('data/initial.csv')
print(f"Loaded {len(df)} rows")
print(df.head())

# Step 2: Add Month column (extract month name from date)
print("\n2. Adding Month column...")
# convert Date column to datetime type first
df['Date'] = pd.to_datetime(df['Date'])
# extract month name like "January", "February", etc.
df['Month'] = df['Date'].dt.strftime('%B')
print("Month column added:")
print(df[['Date', 'Month']].head())

# Step 3: Add Total_Sales (sum all products for each month)
print("\n3. Adding Total_Sales column...")
# sum across the product columns for each row
df['Total_Sales'] = df['Product_A'] + df['Product_B'] + df['Product_C'] + df['Product_D']
print("Total_Sales column added:")
print(df[['Product_A', 'Product_B', 'Product_C', 'Product_D', 'Total_Sales']].head())

# Step 4: Add Average_Sales (average of all products)
print("\n4. Adding Average_Sales column...")
# calculate mean of the 4 products for each row
df['Average_Sales'] = (df['Product_A'] + df['Product_B'] + df['Product_C'] + df['Product_D']) / 4
print("Average_Sales column added:")
print(df[['Total_Sales', 'Average_Sales']].head())

# Step 5: Add Month_over_Month_Growth (percentage change from previous month)
print("\n5. Adding Month_over_Month_Growth column...")
# pct_change() compares each value to the previous one
# multiply by 100 to get percentage
df['Month_over_Month_Growth'] = df['Total_Sales'].pct_change() * 100
print("Growth column added (NaN for first month is normal):")
print(df[['Month', 'Total_Sales', 'Month_over_Month_Growth']].head())

# Step 6: Add Quarter column (Q1, Q2, Q3, Q4)
print("\n6. Adding Quarter column...")
# extract month number (1-12) from date
month_num = df['Date'].dt.month

# assign quarters based on month
# Jan-Mar = Q1, Apr-Jun = Q2, Jul-Sep = Q3, Oct-Dec = Q4
df['Quarter'] = 'Q' + ((month_num - 1) // 3 + 1).astype(str)
print("Quarter column added:")
print(df[['Month', 'Quarter']].head(6))

# Step 7: Find product with max sales each month
print("\n7. Adding Max_Sales_Product column...")
# for each row, find which product column has the max value
product_cols = ['Product_A', 'Product_B', 'Product_C', 'Product_D']
df['Max_Sales_Product'] = df[product_cols].idxmax(axis=1)
print("Max product identified:")
print(df[['Product_A', 'Product_B', 'Product_C', 'Product_D', 'Max_Sales_Product']].head())

# Step 8: Find product with min sales each month
print("\n8. Adding Min_Sales_Product column...")
df['Min_Sales_Product'] = df[product_cols].idxmin(axis=1)
print("Min product identified:")
print(df[['Product_A', 'Product_B', 'Product_C', 'Product_D', 'Min_Sales_Product']].head())

# Step 9: Show the complete enhanced DataFrame
print("\n9. Complete enhanced DataFrame:")
print(df)

# Step 10: Save to Final.csv
print("\n10. Saving to Final.csv...")
df.to_csv('data/Final.csv', index=False)
print("Saved to data/Final.csv")

print("\n" + "=" * 60)
print("Phase 3 Complete!")
print("=" * 60)
print("\nNew columns added:")
print("- Month")
print("- Total_Sales")
print("- Average_Sales")
print("- Month_over_Month_Growth")
print("- Quarter")
print("- Max_Sales_Product")
print("- Min_Sales_Product")
