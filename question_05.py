# Question 5
# Write a function that takes a positive integer and returns the number of digits.

def count_digits(number):
    return len(str(abs(number)))

# Test
test_num = 12345
print(f"Number: {test_num}")
print(f"Number of digits: {count_digits(test_num)}")
