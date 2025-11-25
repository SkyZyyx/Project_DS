"""
Simple tests for utils.py functions
"""

from utils import generate_random_sales, generate_monthly_dates

print("Testing utils functions...")
print()

# Test 1: Check if we get 12 dates
print("Test 1: Dates")
dates = generate_monthly_dates()
print(f"Got {len(dates)} dates")
for i, d in enumerate(dates, 1):
    print(f"  {i}. {d}")
print()

# Test 2: Check sales generation
print("Test 2: Sales generation")
sales = generate_random_sales(50, 100, 12)
print(f"Generated {len(sales)} values")
print(f"Min: {sales.min()}, Max: {sales.max()}")
print(f"Values: {sales}")
print()

# Test 3: Try all products
print("Test 3: All products")
print("Product A:", generate_random_sales(50, 100, 12))
print("Product B:", generate_random_sales(30, 80, 12))
print("Product C:", generate_random_sales(20, 60, 12))
print("Product D:", generate_random_sales(10, 50, 12))

print("\nTests done!")

