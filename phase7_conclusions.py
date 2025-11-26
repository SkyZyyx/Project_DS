"""
Phase 7: Answer conclusion questions
"""

import pandas as pd

df = pd.read_csv('data/Final.csv')

print("=" * 60)
print("Phase 7: Conclusions")
print("=" * 60)

# Question 1: Which product contributes most?
print("\n1. Which product contributes the most to overall sales?")
print("-" * 60)
totals = {
    'A': df['Product_A'].sum(),
    'B': df['Product_B'].sum(),
    'C': df['Product_C'].sum(),
    'D': df['Product_D'].sum()
}
total_all = sum(totals.values())

for prod, amt in totals.items():
    pct = (amt / total_all) * 100
    print(f"Product {prod}: {amt} units ({pct:.1f}%)")

best = max(totals, key=totals.get)
print(f"\nAnswer: Product {best} is the clear winner with {totals[best]} units")
print(f"        It accounts for {(totals[best]/total_all)*100:.1f}% of all sales!")

# Question 2: Which quarter performs best and why?
print("\n\n2. Which quarter performs best and why?")
print("-" * 60)
quarterly = df.groupby('Quarter')['Total_Sales'].sum()
for q, sales in quarterly.items():
    print(f"{q}: {sales} sales")

best_q = quarterly.idxmax()
print(f"\nAnswer: {best_q} performs best with {quarterly[best_q]} sales")
print("Possible reasons:")
print("- End of year / holiday season")
print("- Year-end budget spending")
print("- Seasonal demand patterns")

# Question 3: Strategy recommendations
print("\n\n3. How to improve sales strategy for next year?")
print("-" * 60)
print("Recommendations:")
print()
print("1. Focus on Product A:")
print("   - It's our star product, invest in marketing")
print("   - Ensure good stock levels")
print()
print("2. Improve Product D:")
print(f"   - Only {totals['D']} units sold (weakest)")
print("   - Consider price adjustments or promotions")
print()
print("3. Address Q3 slump:")
quarterly_sorted = quarterly.sort_values()
print(f"   - Q3 had only {quarterly_sorted.iloc[0]} sales")
print("   - Plan summer promotions")
print()
print("4. Leverage Q4 momentum:")
print("   - Q4 was strongest, maintain this trend")
print("   - Start holiday campaigns earlier")

print("\n" + "=" * 60)
print("Analysis Complete!")
print("=" * 60)
