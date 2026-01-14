# Question 20
# Write a Pandas program to find the index of the first occurrence of the smallest and 
# largest value of a given series. If the input is [1, 3, 7, 88, 12, 88, 23, 3, 1, 9, 0], 
# the output should be 0 and 4.

import pandas as pd

# Create a series from the given list
data = [1, 3, 7, 88, 12, 88, 23, 3, 1, 9, 0]
series = pd.Series(data)

print("Given series:")
print(series)
print()

# Find the index of the first occurrence of the smallest value
min_index = series.idxmin()
print(f"Index of first occurrence of smallest value ({series.min()}): {min_index}")

# Find the index of the first occurrence of the largest value
max_index = series.idxmax()
print(f"Index of first occurrence of largest value ({series.max()}): {max_index}")
print()

# Alternative using argmin and argmax from NumPy
import numpy as np
min_index_np = np.argmin(series.values)
max_index_np = np.argmax(series.values)
print("Using NumPy:")
print(f"Index of smallest value: {min_index_np}")
print(f"Index of largest value: {max_index_np}")
