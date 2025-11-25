"""
Monthly Sales Analysis - Phase 2: Data Generation
This is a Python script version of the notebook for easy execution
"""

# ==============================================================================
# 1. SETUP & IMPORTS
# ==============================================================================
print("=" * 70)
print("MONTHLY SALES ANALYSIS - PHASE 2: DATA GENERATION")
print("=" * 70)

# Data manipulation and analysis
import numpy as np
import pandas as pd

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Custom utility functions
from utils import generate_random_sales, generate_monthly_dates

# Set visualization style for better-looking plots
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)

print("\n✅ All libraries imported successfully!")

# ==============================================================================
# 2. DATA GENERATION
# ==============================================================================
print("\n" + "=" * 70)
print("GENERATING DATA")
print("=" * 70)

# Generate 12 monthly dates (Jan 2025 - Dec 2025)
monthly_dates = generate_monthly_dates()

print("\n📅 Generated Monthly Dates:")
for i, date in enumerate(monthly_dates, 1):
    print(f"  Month {i:2d}: {date.strftime('%Y-%m-%d')}")

# Generate random sales for each product (12 months)
# Each product has different sales ranges based on their market performance
print("\n📊 Generating Sales Data...")

sales_product_a = generate_random_sales(min_val=50, max_val=100, size=12)
sales_product_b = generate_random_sales(min_val=30, max_val=80, size=12)
sales_product_c = generate_random_sales(min_val=20, max_val=60, size=12)
sales_product_d = generate_random_sales(min_val=10, max_val=50, size=12)

print("\n📊 Generated Sales Data:")
print(f"Product A (50-100 units): {sales_product_a}")
print(f"Product B (30-80 units):  {sales_product_b}")
print(f"Product C (20-60 units):  {sales_product_c}")
print(f"Product D (10-50 units):  {sales_product_d}")

# ==============================================================================
# 3. CREATE INITIAL DATAFRAME
# ==============================================================================
print("\n" + "=" * 70)
print("CREATING DATAFRAME")
print("=" * 70)

# Create DataFrame with all the data
df_initial = pd.DataFrame({
    'Date': monthly_dates,
    'Product_A': sales_product_a,
    'Product_B': sales_product_b,
    'Product_C': sales_product_c,
    'Product_D': sales_product_d
})

print("\n✅ Initial DataFrame created!")
print(f"\nShape: {df_initial.shape} (rows, columns)")
print("\nFirst few rows:")
print(df_initial.head())

print("\n📋 Complete Initial Dataset:")
print(df_initial)

# ==============================================================================
# 4. SAVE INITIAL DATASET
# ==============================================================================
print("\n" + "=" * 70)
print("SAVING DATA")
print("=" * 70)

# Save to CSV file
df_initial.to_csv('data/initial.csv', index=False)

print("\n✅ Data saved to 'data/initial.csv'")
print(f"   File contains {len(df_initial)} rows of monthly sales data")

# ==============================================================================
# 5. QUICK DATA VALIDATION
# ==============================================================================
print("\n" + "=" * 70)
print("DATA VALIDATION")
print("=" * 70)

# Check basic statistics for each product
print("\n📊 Sales Statistics Summary:\n")
print(df_initial[['Product_A', 'Product_B', 'Product_C', 'Product_D']].describe())

print("\n✅ Validation:")
print(f"   Product A range: {df_initial['Product_A'].min()}-{df_initial['Product_A'].max()} (expected: 50-100)")
print(f"   Product B range: {df_initial['Product_B'].min()}-{df_initial['Product_B'].max()} (expected: 30-80)")
print(f"   Product C range: {df_initial['Product_C'].min()}-{df_initial['Product_C'].max()} (expected: 20-60)")
print(f"   Product D range: {df_initial['Product_D'].min()}-{df_initial['Product_D'].max()} (expected: 10-50)")

# ==============================================================================
# PHASE 1 COMPLETE
# ==============================================================================
print("\n" + "=" * 70)
print("✅ PHASE 2 COMPLETE!")
print("=" * 70)

print("""
What we've accomplished:
- ✅ Generated 12 monthly dates
- ✅ Created random sales data for 4 products
- ✅ Built initial DataFrame
- ✅ Saved to 'data/initial.csv'
- ✅ Validated data ranges

Next Steps: 
- Enhance DataFrame with calculated metrics
- Add quarterly information
- Identify max/min products per month
""")
