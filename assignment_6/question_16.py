# Question 16
# Write a NumPy program to create a 9*9*2 array with random values and extract any array 
# of shape (5,5,2) from the said array.

import numpy as np

# Create a 9x9x2 array with random values
np.random.seed(42)
array_9x9x2 = np.random.rand(9, 9, 2)

print("Original 9x9x2 array shape:", array_9x9x2.shape)
print("First slice [:,:,0] of the array:")
print(array_9x9x2[:, :, 0])
print()

# Extract a 5x5x2 array from the 9x9x2 array
# We can start from different positions - let's extract from position (2, 2)
start_row = 2
start_col = 2
extracted_array = array_9x9x2[start_row:start_row+5, start_col:start_col+5, :]

print(f"Extracted 5x5x2 array (from position [{start_row}, {start_col}]):")
print("Shape:", extracted_array.shape)
print("First slice [:,:,0] of the extracted array:")
print(extracted_array[:, :, 0])
print()

# Another example: extract from top-left corner (0, 0)
extracted_array2 = array_9x9x2[0:5, 0:5, :]
print("Extracted 5x5x2 array (from position [0, 0]):")
print("Shape:", extracted_array2.shape)
print("First slice [:,:,0]:")
print(extracted_array2[:, :, 0])
print()

# Another example: extract from bottom-right corner
extracted_array3 = array_9x9x2[4:9, 4:9, :]
print("Extracted 5x5x2 array (from position [4, 4]):")
print("Shape:", extracted_array3.shape)
print("First slice [:,:,0]:")
print(extracted_array3[:, :, 0])
