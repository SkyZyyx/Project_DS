import numpy as np
from datetime import date
from dateutil.relativedelta import relativedelta

# generate random sales data
def generate_random_sales(min_val, max_val, size):
    # need to add 1 because randint doesn't include the max value
    return np.random.randint(min_val, max_val + 1, size)

# create the 12 monthly dates for the year
def generate_monthly_dates():
    start_date = date(2025, 1, 1)
    monthly_dates = []
    
    for i in range(12):
        monthly_dates.append(start_date + relativedelta(months=i))
    
    return monthly_dates