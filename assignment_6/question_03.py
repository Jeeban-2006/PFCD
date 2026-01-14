# Question 3
# Create a 3-by-3 array containing the even integers from 2 through 18. Create a second 
# 3-by-3 array containing the integers from 9 down to 1, then multiply the first array 
# by the second.

import numpy as np

# Create first 3-by-3 array with even integers from 2 through 18
array1 = np.arange(2, 19, 2).reshape(3, 3)
print("First array (even integers 2-18):")
print(array1)
print()

# Create second 3-by-3 array with integers from 9 down to 1
array2 = np.arange(9, 0, -1).reshape(3, 3)
print("Second array (integers 9-1):")
print(array2)
print()

# Multiply the first array by the second (element-wise)
result = array1 * array2
print("Result of multiplication (element-wise):")
print(result)
