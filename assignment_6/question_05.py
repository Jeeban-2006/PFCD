# Question 5
# Create a 2-by-5 array from an argument which is a list of the two five-element lists 
# [2, 3, 5, 7, 11] and [13, 17, 19, 23, 29].

import numpy as np

# Create list of two five-element lists
list_data = [[2, 3, 5, 7, 11], [13, 17, 19, 23, 29]]

# Create 2-by-5 array from the list
array = np.array(list_data)

print("2-by-5 array from list:")
print(array)
print()
print(f"Shape: {array.shape}")
print(f"Data type: {array.dtype}")
