"""
Phase 6: Visualizations
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load data
df = pd.read_csv('data/Final.csv')

# setup
sns.set_style('whitegrid')

# 1. Line chart - products over time
print("Creating line chart...")
plt.figure(figsize=(12, 6))
plt.plot(df['Month'], df['Product_A'], marker='o', label='Product A')
plt.plot(df['Month'], df['Product_B'], marker='s', label='Product B')
plt.plot(df['Month'], df['Product_C'], marker='^', label='Product C')
plt.plot(df['Month'], df['Product_D'], marker='d', label='Product D')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Monthly Sales by Product')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('data/line_chart.png')
print("Saved: line_chart.png")
plt.close()

# 2. Stacked bar chart
print("Creating stacked bar chart...")
plt.figure(figsize=(12, 6))
products = df[['Product_A', 'Product_B', 'Product_C', 'Product_D']]
products.plot(kind='bar', stacked=True, ax=plt.gca())
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.title('Stacked Monthly Sales')
plt.xticks(range(12), df['Month'], rotation=45)
plt.legend(title='Products')
plt.tight_layout()
plt.savefig('data/stacked_bar.png')
print("Saved: stacked_bar.png")
plt.close()

# 3. Heatmap
print("Creating heatmap...")
plt.figure(figsize=(10, 6))
heat_data = df[['Product_A', 'Product_B', 'Product_C', 'Product_D']].T
heat_data.columns = df['Month']
sns.heatmap(heat_data, annot=True, fmt='d', cmap='YlOrRd')
plt.title('Sales Heatmap')
plt.ylabel('Product')
plt.xlabel('Month')
plt.tight_layout()
plt.savefig('data/heatmap.png')
print("Saved: heatmap.png")
plt.close()

# 4. Boxplot
print("Creating boxplot...")
plt.figure(figsize=(10, 6))
box_data = df[['Product_A', 'Product_B', 'Product_C', 'Product_D']]
sns.boxplot(data=box_data)
plt.ylabel('Sales')
plt.title('Sales Distribution by Product')
plt.tight_layout()
plt.savefig('data/boxplot.png')
print("Saved: boxplot.png")
plt.close()

print("\nAll visualizations saved to data/ folder!")
