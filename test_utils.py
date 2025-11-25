"""
Test script for utils.py functions
This helps verify our functions work correctly before using them in the main project
"""

from utils import generate_random_sales, generate_monthly_dates
import numpy as np

print("=" * 60)
print("Testing utils.py functions")
print("=" * 60)

# Test 1: generate_monthly_dates()
print("\n📅 Test 1: generate_monthly_dates()")
print("-" * 60)
monthly_dates = generate_monthly_dates()

print(f"✅ Generated {len(monthly_dates)} dates")
print(f"First date: {monthly_dates[0]}")
print(f"Last date: {monthly_dates[-1]}")
print("\nAll dates:")
for i, d in enumerate(monthly_dates, 1):
    print(f"  Month {i:2d}: {d.strftime('%Y-%m-%d')}")

# Test 2: generate_random_sales() - Product A (50-100)
print("\n📊 Test 2: generate_random_sales() - Product A")
print("-" * 60)
sales_a = generate_random_sales(min_val=50, max_val=100, size=12)

print(f"✅ Generated {len(sales_a)} sales values")
print(f"Type: {type(sales_a)}")
print(f"Min value: {sales_a.min()} (expected: >= 50)")
print(f"Max value: {sales_a.max()} (expected: <= 100)")
print(f"Sales values: {sales_a}")

# Test 3: generate_random_sales() - All products
print("\n📦 Test 3: Generate sales for all 4 products")
print("-" * 60)

products = {
    'Product A': (50, 100),
    'Product B': (30, 80),
    'Product C': (20, 60),
    'Product D': (10, 50)
}

for product_name, (min_val, max_val) in products.items():
    sales = generate_random_sales(min_val, max_val, size=12)
    print(f"{product_name} [{min_val:3d}-{max_val:3d}]: min={sales.min():3d}, max={sales.max():3d}, avg={sales.mean():6.2f}")

# Test 4: Verify randomness (run function twice, should get different results)
print("\n🎲 Test 4: Verify randomness")
print("-" * 60)
sales_1 = generate_random_sales(50, 100, 5)
sales_2 = generate_random_sales(50, 100, 5)
print(f"First run:  {sales_1}")
print(f"Second run: {sales_2}")
print(f"Are they different? {not np.array_equal(sales_1, sales_2)} (should be True)")

print("\n" + "=" * 60)
print("✅ All tests completed successfully!")
print("=" * 60)
