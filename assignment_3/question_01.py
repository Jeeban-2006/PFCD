# Question 1
# Write a Python function to find the first, second and third greatest digit in a number.
# Sample Number: 6328
# Expected Output: 8, 6, 3

def find_top_three_digits(number):
    digits = sorted(str(abs(number)), reverse=True)
    return int(digits[0]), int(digits[1]), int(digits[2])

# Test
result = find_top_three_digits(6328)
print(f"First, Second, Third greatest digits: {result[0]}, {result[1]}, {result[2]}")
