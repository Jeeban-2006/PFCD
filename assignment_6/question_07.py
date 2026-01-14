# Question 7
# Find the most frequent values in an array of positive integers. 
# The original array is [6 9 5 1 7 5 1 0 1 5 5 0 8 9 0 7 0 7 6 5 1 1 9 5 3 8 7 9 6 3 4 5 9 7 2 7 0 2 2 6].

import numpy as np

# Original array
array = np.array([6, 9, 5, 1, 7, 5, 1, 0, 1, 5, 5, 0, 8, 9, 0, 7, 0, 7, 6, 5, 
                  1, 1, 9, 5, 3, 8, 7, 9, 6, 3, 4, 5, 9, 7, 2, 7, 0, 2, 2, 6])

print("Original array:")
print(array)
print()

# Count occurrences of each unique value
unique_values, counts = np.unique(array, return_counts=True)

print("Unique values and their counts:")
for value, count in zip(unique_values, counts):
    print(f"Value {value}: appears {count} times")
print()

# Find the maximum frequency
max_count = np.max(counts)
print(f"Maximum frequency: {max_count}")

# Find all values with maximum frequency
most_frequent_values = unique_values[counts == max_count]
print(f"Most frequent value(s): {most_frequent_values}")
print()

# Alternative using bincount for non-negative integers
print("Using bincount:")
count_array = np.bincount(array)
print(f"Count array: {count_array}")
print(f"Most frequent value: {np.argmax(count_array)}")
print(f"Frequency: {np.max(count_array)}")
