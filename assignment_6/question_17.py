# Question 17
# Write a code to create a 4*4 array with random values and sort each column.

import numpy as np

# Create a 4x4 array with random values
np.random.seed(42)
array = np.random.rand(4, 4)

print("Original 4x4 array:")
print(array)
print()

# Sort each column
# np.sort sorts along axis=0 (rows), which sorts each column
sorted_array = np.sort(array, axis=0)

print("Array after sorting each column:")
print(sorted_array)
print()

# Alternative: using argsort to see the indices
print("Verification - each column is sorted in ascending order:")
for col in range(4):
    print(f"Column {col}: {sorted_array[:, col]}")
