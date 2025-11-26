"""
Phase 4: Pivot tables for quarterly analysis
"""

import pandas as pd

print("=" * 60)
print("Phase 4: Quarterly Analysis")
print("=" * 60)

# load the data from phase 3
print("\n1. Loading data...")
df = pd.read_csv('data/Final.csv')
print(f"Loaded {len(df)} rows")

# pivot table: average sales per product per quarter
print("\n2. Average sales by quarter:")
pivot_avg = df.pivot_table(
    values=['Product_A', 'Product_B', 'Product_C', 'Product_D'],
    index='Quarter',
    aggfunc='mean'
)
print(pivot_avg)

# total sales per quarter
print("\n3. Total sales per quarter:")
quarterly_totals = df.groupby('Quarter')['Total_Sales'].sum()
print(quarterly_totals)

# find best quarter
best_q = quarterly_totals.idxmax()
print(f"\nBest quarter: {best_q} ({quarterly_totals.max()} sales)")

# combine everything into one summary
summary = pd.DataFrame({
    'Total_Sales': quarterly_totals,
    'Avg_A': pivot_avg['Product_A'],
    'Avg_B': pivot_avg['Product_B'],
    'Avg_C': pivot_avg['Product_C'],
    'Avg_D': pivot_avg['Product_D']
})

print("\n4. Summary:")
print(summary)

# save to output.csv
print("\n5. Saving...")
with open('data/output.csv', 'w') as f:
    f.write("QUARTERLY SUMMARY\n\n")
summary.to_csv('data/output.csv', mode='a')

with open('data/output.csv', 'a') as f:
    f.write("\n\nMONTHLY DATA\n\n")
df.to_csv('data/output.csv', mode='a', index=False)

print("Saved to data/output.csv")

print("\n" + "=" * 60)
print("Done!")
print(f"Best: {best_q}, Worst: {quarterly_totals.idxmin()}")
print("=" * 60)
