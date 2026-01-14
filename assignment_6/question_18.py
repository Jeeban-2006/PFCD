# Question 18
# Write a Pandas program to convert the first column of a DataFrame as a Series.

import pandas as pd
import numpy as np

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45],
    'City': ['New York', 'London', 'Paris', 'Tokyo', 'Sydney'],
    'Salary': [50000, 60000, 75000, 80000, 90000]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print()

# Convert the first column to a Series
# Method 1: Using iloc
first_column_series1 = df.iloc[:, 0]
print("First column as Series (using iloc):")
print(first_column_series1)
print(f"Type: {type(first_column_series1)}")
print()

# Method 2: Using column name
first_column_series2 = df['Name']
print("First column as Series (using column name):")
print(first_column_series2)
print(f"Type: {type(first_column_series2)}")
print()

# Method 3: Using squeeze() to convert single column DataFrame to Series
first_column_series3 = df[['Name']].squeeze()
print("First column as Series (using squeeze):")
print(first_column_series3)
print(f"Type: {type(first_column_series3)}")
