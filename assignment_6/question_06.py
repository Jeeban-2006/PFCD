# Question 6
# Create a 2-by-3 array containing the first six powers of 2 beginning with 2^0. 
# Flatten the array first with method flatten, then with ravel. In each case, display 
# the result then display the original array to show that it was unmodified.

import numpy as np

# Create 2-by-3 array with first six powers of 2 (2^0 to 2^5)
original_array = np.array([2**i for i in range(6)]).reshape(2, 3)
print("Original array (powers of 2):")
print(original_array)
print()

# Using flatten() - creates a copy
flattened = original_array.flatten()
print("Flattened array (using flatten):")
print(flattened)
print()

# Modify the flattened array to show it's a copy
flattened[0] = 999
print("After modifying flattened array:")
print("Flattened:", flattened)
print("Original (unchanged):", original_array)
print()

# Using ravel() - returns a view
raveled = original_array.ravel()
print("Raveled array (using ravel):")
print(raveled)
print()

# Note: ravel returns a view, so modifying it would affect the original
# But we'll create a fresh ravel for demonstration
original_array = np.array([2**i for i in range(6)]).reshape(2, 3)
raveled = original_array.ravel()
print("After using ravel:")
print("Raveled:", raveled)
print("Original (unchanged):", original_array)
print()

print("Key difference:")
print("- flatten() creates a copy (modifications don't affect original)")
print("- ravel() returns a view (modifications may affect original)")
