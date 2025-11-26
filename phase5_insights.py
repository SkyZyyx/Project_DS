"""
Phase 5: Key insights - finding best month/product/quarter
"""

import pandas as pd

print("=" * 60)
print("Phase 5: Finding Key Insights")
print("=" * 60)

# load the data
df = pd.read_csv('data/Final.csv')

# 1. Best month (highest total sales)
print("\n1. Best Month:")
best_month_idx = df['Total_Sales'].idxmax()
best_month = df.loc[best_month_idx, 'Month']
best_month_sales = df.loc[best_month_idx, 'Total_Sales']
print(f"   {best_month}: {best_month_sales} sales")

# 2. Best product (highest annual sales)
print("\n2. Best Product (total for the year):")
annual_sales = {
    'Product_A': df['Product_A'].sum(),
    'Product_B': df['Product_B'].sum(),
    'Product_C': df['Product_C'].sum(),
    'Product_D': df['Product_D'].sum()
}
print("   Annual totals:")
for product, total in annual_sales.items():
    print(f"   - {product}: {total}")

best_product = max(annual_sales, key=annual_sales.get)
print(f"\n   Winner: {best_product} with {annual_sales[best_product]} units")

# 3. Best quarter
print("\n3. Best Quarter:")
quarterly = df.groupby('Quarter')['Total_Sales'].sum()
best_quarter = quarterly.idxmax()
print(f"   {best_quarter}: {quarterly[best_quarter]} sales")

print("\n" + "=" * 60)
print("Summary:")
print(f"Best Month: {best_month}")
print(f"Best Product: {best_product}")
print(f"Best Quarter: {best_quarter}")
print("=" * 60)
