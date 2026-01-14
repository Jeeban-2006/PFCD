# Question 9
# Write a function format_2d_array(arr) that takes a two-dimensional array of positive 
# integers (represented as nested lists) and returns a formatted string that mimics NumPy's 
# column-based format. In this format, each element in the array should be right-aligned, 
# and the width of each column should be determined by the number of characters required 
# to display the largest element in the array.

import numpy as np

def format_2d_array(arr):
    # Convert to numpy array if it's a list
    if isinstance(arr, list):
        arr = np.array(arr)
    
    # Find the maximum number of digits in the array
    max_width = len(str(np.max(arr)))
    
    # Create formatted string
    result = []
    for row in arr:
        formatted_row = ' '.join([f"{elem:>{max_width}}" for elem in row])
        result.append(formatted_row)
    
    return '\n'.join(result)

# Test with examples
test_array1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Test Array 1:")
print(format_2d_array(test_array1))
print()

test_array2 = [[10, 200, 3000], [40, 500, 6000], [7, 80, 900]]
print("Test Array 2:")
print(format_2d_array(test_array2))
print()

test_array3 = [[1, 22, 333, 4444], [55, 666, 7777, 88888]]
print("Test Array 3:")
print(format_2d_array(test_array3))
print()

# Compare with NumPy's default format
print("NumPy's format for test_array2:")
print(np.array(test_array2))
