# Question 15
# Write functions median and mode that use existing NumPy capabilities to determine the 
# median (middle) and mode (most frequent) of the values in an array. Your functions should 
# determine the median and mode regardless of the array's shape.

import numpy as np
from scipy import stats

def median(array):
    """Calculate the median of an array regardless of its shape."""
    return np.median(array)

def mode(array):
    """Calculate the mode (most frequent value) of an array regardless of its shape."""
    # Flatten the array
    flattened = array.flatten()
    
    # Use scipy.stats.mode for finding the most frequent value
    mode_result = stats.mode(flattened, keepdims=True)
    return mode_result.mode[0]

# Alternative mode function using only NumPy
def mode_numpy_only(array):
    """Calculate mode using only NumPy (without scipy)."""
    flattened = array.flatten()
    unique_values, counts = np.unique(flattened, return_counts=True)
    max_count = np.max(counts)
    mode_value = unique_values[counts == max_count][0]
    return mode_value

# Test the functions
print("Test 1: 1D array")
array1 = np.array([1, 2, 3, 3, 4, 5, 3, 6, 7, 3])
print(f"Array: {array1}")
print(f"Median: {median(array1)}")
print(f"Mode: {mode(array1)}")
print()

print("Test 2: 2D array")
array2 = np.array([[1, 2, 3], [4, 5, 5], [5, 5, 9]])
print(f"Array:\n{array2}")
print(f"Median: {median(array2)}")
print(f"Mode: {mode(array2)}")
print()

print("Test 3: 3D array")
array3 = np.array([[[1, 2], [3, 3]], [[3, 4], [5, 3]]])
print(f"Array:\n{array3}")
print(f"Median: {median(array3)}")
print(f"Mode: {mode(array3)}")
print()

# Test mode_numpy_only
print("Test 4: Using NumPy-only mode function")
print(f"Mode (NumPy only): {mode_numpy_only(array1)}")
