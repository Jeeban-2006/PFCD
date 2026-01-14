# Question 4
# Create a 2D array and swap the first two rows and two columns.

import numpy as np

# Create a 2D array (4x4 for demonstration)
array = np.arange(1, 17).reshape(4, 4)
print("Original array:")
print(array)
print()

# Swap the first two rows
array[[0, 1]] = array[[1, 0]]
print("After swapping first two rows:")
print(array)
print()

# Swap the first two columns
array[:, [0, 1]] = array[:, [1, 0]]
print("After swapping first two columns:")
print(array)
