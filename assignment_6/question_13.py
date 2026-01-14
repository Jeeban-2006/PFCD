# Question 13
# Use NumPy's tile function to create a checkerboard pattern of dashes and asterisks.

import numpy as np

# Create a 2x2 pattern of dashes and asterisks
pattern = np.array([['-', '*'], ['*', '-']])

print("Basic 2x2 pattern:")
print(pattern)
print()

# Create a checkerboard using tile (repeat the pattern)
# 4x4 checkerboard (repeat 2x2 pattern 2 times in each direction)
checkerboard_4x4 = np.tile(pattern, (2, 2))
print("4x4 checkerboard:")
for row in checkerboard_4x4:
    print(' '.join(row))
print()

# 8x8 checkerboard (repeat 2x2 pattern 4 times in each direction)
checkerboard_8x8 = np.tile(pattern, (4, 4))
print("8x8 checkerboard:")
for row in checkerboard_8x8:
    print(' '.join(row))
print()

# Alternative: using 1s and 0s
pattern_numeric = np.array([[0, 1], [1, 0]])
checkerboard_numeric = np.tile(pattern_numeric, (4, 4))
print("8x8 checkerboard (numeric):")
print(checkerboard_numeric)
