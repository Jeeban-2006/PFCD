# Question 22
# Perform the following tasks using the pandas Series object:
# (a) Create a Series from the list [7, 11, 13, 17].
# (b) Create a Series with five elements where each element is 100.0.
# (c) Create a Series with 20 elements that are all random numbers in the range 0 to 100. 
#     Use the describe method to produce the Series' basic descriptive statistics.
# (d) Create a Series called temperatures with the following floating-point values: 98.6, 98.9, 
#     100.2, and 97.9. Use the index keyword argument to specify the custom indices 'Julie', 
#     'Charlie', 'Sam', and 'Andrea'.
# (e) Form a dictionary from the names and values in Part (d), then use it to initialize a Series.

import pandas as pd
import numpy as np

# (a) Create a Series from the list [7, 11, 13, 17]
print("(a) Series from list [7, 11, 13, 17]:")
series_a = pd.Series([7, 11, 13, 17])
print(series_a)
print()

# (b) Create a Series with five elements where each element is 100.0
print("(b) Series with five elements of 100.0:")
series_b = pd.Series([100.0] * 5)
# or: series_b = pd.Series(100.0, index=range(5))
print(series_b)
print()

# (c) Create a Series with 20 elements that are random numbers in range 0-100
print("(c) Series with 20 random numbers (0-100):")
np.random.seed(42)
series_c = pd.Series(np.random.randint(0, 101, size=20))
print(series_c)
print("\nDescriptive statistics:")
print(series_c.describe())
print()

# (d) Create Series with custom indices
print("(d) Series 'temperatures' with custom indices:")
temperatures = pd.Series([98.6, 98.9, 100.2, 97.9], 
                        index=['Julie', 'Charlie', 'Sam', 'Andrea'])
print(temperatures)
print()

# (e) Form a dictionary and initialize a Series
print("(e) Series from dictionary:")
temp_dict = {
    'Julie': 98.6,
    'Charlie': 98.9,
    'Sam': 100.2,
    'Andrea': 97.9
}
series_e = pd.Series(temp_dict)
print(series_e)
