# Question 2
# Use arange to create a 2-by-2 array containing the numbers 0-3. Use broadcasting to 
# perform each of the following operations on the original array:
# (a) Cube every element of the array.
# (b) Add 7 to every element of the array.
# (c) Multiply every element of the array by 2.

import numpy as np

# Create a 2-by-2 array containing numbers 0-3
original_array = np.arange(4).reshape(2, 2)
print("Original array:")
print(original_array)
print()

# (a) Cube every element of the array
cubed_array = original_array ** 3
print("(a) Cubed array:")
print(cubed_array)
print()

# (b) Add 7 to every element of the array
added_array = original_array + 7
print("(b) Array after adding 7:")
print(added_array)
print()

# (c) Multiply every element of the array by 2
multiplied_array = original_array * 2
print("(c) Array after multiplying by 2:")
print(multiplied_array)
