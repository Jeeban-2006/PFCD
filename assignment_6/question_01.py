# Question 1
# Create a 2-by-3 array with ones, a 3-by-3 array with zeros and a 2-by-5 array with sevens.

import numpy as np

# Create a 2-by-3 array with ones
array_ones = np.ones((2, 3))
print("2-by-3 array with ones:")
print(array_ones)
print()

# Create a 3-by-3 array with zeros
array_zeros = np.zeros((3, 3))
print("3-by-3 array with zeros:")
print(array_zeros)
print()

# Create a 2-by-5 array with sevens
array_sevens = np.full((2, 5), 7)
print("2-by-5 array with sevens:")
print(array_sevens)
