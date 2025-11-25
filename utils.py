import numpy as np
from datetime import date
from dateutil.relativedelta import relativedelta

# Function that returns random numpy array of integers between min_val and max_val for the given size 

def generate_random_sales(min_val, max_val, size):
    """
    Generate random sales data using NumPy.
    
    Parameters:
    - min_val: minimum sales value (inclusive)
    - max_val: maximum sales value (inclusive)
    - size: number of data points to generate
    
    Returns:
    - NumPy array of random integers
    """
    # Note: np.random.randint is exclusive of the upper bound, so we add 1
    return np.random.randint(min_val, max_val + 1, size)

# Function that generates 12 monthly dates 

def generate_monthly_dates():
    """
    Generate 12 monthly dates starting from January 1, 2025.
    
    Returns:
    - List of date objects for each month
    """
    # The start date is first january 2025 
    start_date = date(2025, 1, 1)

    # We create a list to store the 12 monthly dates 
    monthly_dates = []

    # We loop over the 12 months and append the date to the list 
    for i in range(12):
        monthly_dates.append(start_date + relativedelta(months=i))
    
    return monthly_dates