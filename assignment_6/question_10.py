# Question 10
# Create an array containing the values 1-15, reshape it into a 3-by-5 array, then use 
# indexing and slicing techniques to perform each of the following operations:
# (a) Select row 2.
# (b) Select column 5.
# (c) Select rows 0 and 1.
# (d) Select columns 2-4.
# (e) Select the element that is in row 1 and column 4.
# (f) Select all elements from rows 1 and 2 that are in columns 0, 2 and 4.

import numpy as np

# Create array with values 1-15 and reshape to 3-by-5
array = np.arange(1, 16).reshape(3, 5)

print("Original array:")
print(array)
print()

# (a) Select row 2
print("(a) Select row 2:")
print(array[2])
print()

# (b) Select column 5 (index 4, as columns are 0-indexed)
print("(b) Select column 5 (index 4):")
print(array[:, 4])
print()

# (c) Select rows 0 and 1
print("(c) Select rows 0 and 1:")
print(array[0:2])
# or: print(array[[0, 1]])
print()

# (d) Select columns 2-4 (indices 1, 2, 3)
print("(d) Select columns 2-4 (indices 1, 2, 3):")
print(array[:, 1:4])
print()

# (e) Select the element that is in row 1 and column 4 (indices 1, 3)
print("(e) Select element in row 1 and column 4 (indices [1, 3]):")
print(array[1, 3])
print()

# (f) Select all elements from rows 1 and 2 that are in columns 0, 2 and 4
print("(f) Select elements from rows 1 and 2 in columns 0, 2 and 4:")
print(array[1:3, [0, 2, 4]])
# or using ix_: print(array[np.ix_([1, 2], [0, 2, 4])])
