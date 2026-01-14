# Question 8
# (needs to change) Use linspace and reshape to create a 2-by-3 array with the values 
# 1.1, 2.2, ..., 6.6. Then use astype to convert the array to an array of integers.

import numpy as np

# Create array using linspace
# linspace(start, stop, num) creates num evenly spaced values from start to stop
array_float = np.linspace(1.1, 6.6, 6).reshape(2, 3)

print("Original array (float):")
print(array_float)
print(f"Data type: {array_float.dtype}")
print()

# Convert to integers using astype
array_int = array_float.astype(int)

print("Converted array (integer):")
print(array_int)
print(f"Data type: {array_int.dtype}")
