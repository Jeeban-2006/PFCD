# Question 11
# Given the following two-dimensional arrays in NumPy:
# array1 = np.array([[0, 1], [2, 3]])
# array2 = np.array([[4, 5], [6, 7]])
# Perform the following tasks:
# (a) Use vertical stacking to create a 4-by-2 array named array3, with array1 stacked on top of array2.
# (b) Use horizontal stacking to create a 2-by-4 array named array4, with array2 to the right of array1.
# (c) Use vertical stacking with two copies of array4 to create a 4-by-4 array named array5.
# (d) Use horizontal stacking with two copies of array3 to create a 4-by-4 array named array6.

import numpy as np

# Create the arrays
array1 = np.array([[0, 1], [2, 3]])
array2 = np.array([[4, 5], [6, 7]])

print("Array 1:")
print(array1)
print()
print("Array 2:")
print(array2)
print()

# (a) Use vertical stacking to create array3
array3 = np.vstack((array1, array2))
print("(a) array3 (vertical stacking - array1 on top of array2):")
print(array3)
print(f"Shape: {array3.shape}")
print()

# (b) Use horizontal stacking to create array4
array4 = np.hstack((array1, array2))
print("(b) array4 (horizontal stacking - array2 to the right of array1):")
print(array4)
print(f"Shape: {array4.shape}")
print()

# (c) Use vertical stacking with two copies of array4 to create array5
array5 = np.vstack((array4, array4))
print("(c) array5 (vertical stacking of two copies of array4):")
print(array5)
print(f"Shape: {array5.shape}")
print()

# (d) Use horizontal stacking with two copies of array3 to create array6
array6 = np.hstack((array3, array3))
print("(d) array6 (horizontal stacking of two copies of array3):")
print(array6)
print(f"Shape: {array6.shape}")
