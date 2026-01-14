# Question 4
# Write a function that takes a string as input and returns the reversed string.

def reverse_string(s):
    return s[::-1]

# Test
test_string = "Hello World"
print(f"Original: {test_string}")
print(f"Reversed: {reverse_string(test_string)}")
