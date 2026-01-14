# Question 14
# Use the NumPy bincount function to count the number of occurrences of each non-negative 
# integer in a 5-by-5 array of random integers in the range 0 - 99.

import numpy as np

# Create a 5-by-5 array of random integers in the range 0-99
np.random.seed(42)  # For reproducibility
array = np.random.randint(0, 100, size=(5, 5))

print("5-by-5 array of random integers (0-99):")
print(array)
print()

# Flatten the array and use bincount
flattened = array.flatten()
counts = np.bincount(flattened)

print("Occurrences of each value (using bincount):")
print(f"Length of count array: {len(counts)}")
print()

# Display only the values that actually appear
print("Values that appear in the array:")
for value, count in enumerate(counts):
    if count > 0:
        print(f"Value {value}: appears {count} time(s)")
print()

# Total count verification
print(f"Total elements: {np.sum(counts)} (should be 25)")
print()

# Alternative visualization
print("Summary statistics:")
unique_values, unique_counts = np.unique(array, return_counts=True)
print(f"Number of unique values: {len(unique_values)}")
print(f"Most common value: {unique_values[np.argmax(unique_counts)]}")
print(f"Frequency of most common: {np.max(unique_counts)}")
