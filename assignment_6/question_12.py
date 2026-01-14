# Question 12
# Use NumPy's concatenate Function to reimplement the previous problem.

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

# (a) Use concatenate for vertical stacking (axis=0)
array3 = np.concatenate((array1, array2), axis=0)
print("(a) array3 (concatenate with axis=0 - vertical stacking):")
print(array3)
print(f"Shape: {array3.shape}")
print()

# (b) Use concatenate for horizontal stacking (axis=1)
array4 = np.concatenate((array1, array2), axis=1)
print("(b) array4 (concatenate with axis=1 - horizontal stacking):")
print(array4)
print(f"Shape: {array4.shape}")
print()

# (c) Use concatenate with two copies of array4 (axis=0)
array5 = np.concatenate((array4, array4), axis=0)
print("(c) array5 (concatenate two copies of array4 with axis=0):")
print(array5)
print(f"Shape: {array5.shape}")
print()

# (d) Use concatenate with two copies of array3 (axis=1)
array6 = np.concatenate((array3, array3), axis=1)
print("(d) array6 (concatenate two copies of array3 with axis=1):")
print(array6)
print(f"Shape: {array6.shape}")
