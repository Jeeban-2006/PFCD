# Question 19
# Convert s1=[1,2,3,4,2] and s2=[3,4,5,6] to two series objects. Find elements in s1, 
# which are not present in s2.

import pandas as pd
import numpy as np

# Create two lists
s1_list = [1, 2, 3, 4, 2]
s2_list = [3, 4, 5, 6]

# Convert to series objects
s1 = pd.Series(s1_list)
s2 = pd.Series(s2_list)

print("Series s1:")
print(s1)
print()

print("Series s2:")
print(s2)
print()

# Find elements in s1 which are not present in s2
# Method 1: Using isin() and boolean indexing
elements_not_in_s2_method1 = s1[~s1.isin(s2)]
print("Elements in s1 not present in s2 (Method 1 - using isin):")
print(elements_not_in_s2_method1)
print()

# Method 2: Using set difference
unique_in_s1 = set(s1) - set(s2)
print("Elements in s1 not present in s2 (Method 2 - using set difference):")
print(unique_in_s1)
print()

# Method 3: Get unique values only
elements_not_in_s2_unique = s1[~s1.isin(s2)].unique()
print("Unique elements in s1 not present in s2:")
print(elements_not_in_s2_unique)
