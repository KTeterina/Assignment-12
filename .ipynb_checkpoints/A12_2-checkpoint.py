import numpy as np
import pandas as pd

# Company income for 10 months
income = np.array([10000, 12000, 15000, 13000, 11000, 14000, 16000, 12000, 18000, 15000])

# Income without tax
income_without_tax = income * 0.7

# Company expenses for 10 months
expenses = np.array([8000, 9000, 11000, 10000, 8000, 12000, 13000, 9000, 14000, 12000])

# Months
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'])

# Create a DataFrame
df = pd.DataFrame({
  'Month': months,
  'Income Without Tax': income_without_tax,
  'Expenses': expenses
})

# Output the entire DataFrame
print("Complete DataFrame:")
print(df)

# Output 1st quarter data
print("\n1st Quarter Data:")
print(df.iloc[:3])
