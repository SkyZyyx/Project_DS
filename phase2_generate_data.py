"""
Monthly Sales Analysis - Data Generation
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils import generate_random_sales, generate_monthly_dates

# set some style preferences
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)

print("=" * 60)
print("Monthly Sales Analysis - Generating Data")
print("=" * 60)

# Step 1: Generate the dates
print("\n1. Generating monthly dates...")
monthly_dates = generate_monthly_dates()

print(f"Created {len(monthly_dates)} dates:")
for i, date in enumerate(monthly_dates, 1):
    print(f"  {i:2d}. {date.strftime('%Y-%m-%d')}")

# Step 2: Generate sales for each product
print("\n2. Generating random sales data...")

# each product has different sales ranges
sales_a = generate_random_sales(50, 100, 12)
sales_b = generate_random_sales(30, 80, 12)
sales_c = generate_random_sales(20, 60, 12)
sales_d = generate_random_sales(10, 50, 12)

print(f"Product A: {sales_a}")
print(f"Product B: {sales_b}")
print(f"Product C: {sales_c}")
print(f"Product D: {sales_d}")

# Step 3: Create the DataFrame
print("\n3. Creating DataFrame...")

df = pd.DataFrame({
    'Date': monthly_dates,
    'Product_A': sales_a,
    'Product_B': sales_b,
    'Product_C': sales_c,
    'Product_D': sales_d
})

print(f"Shape: {df.shape}")
print("\nFirst rows:")
print(df.head())

print("\nAll data:")
print(df)

# Step 4: Save it
print("\n4. Saving to CSV...")
df.to_csv('data/initial.csv', index=False)
print("Saved to data/initial.csv")

# Step 5: Quick check
print("\n5. Data validation:")
print(df[['Product_A', 'Product_B', 'Product_C', 'Product_D']].describe())

print("\nRanges:")
print(f"Product A: {df['Product_A'].min()}-{df['Product_A'].max()} ✓")
print(f"Product B: {df['Product_B'].min()}-{df['Product_B'].max()} ✓")
print(f"Product C: {df['Product_C'].min()}-{df['Product_C'].max()} ✓")
print(f"Product D: {df['Product_D'].min()}-{df['Product_D'].max()} ✓")

print("\n" + "=" * 60)
print("Done! ")
print("=" * 60)

