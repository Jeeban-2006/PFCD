# Question 30
# Write a function that inputs a number and returns the product of digits of that number.

def product_of_digits(number):
    product = 1
    for digit in str(abs(number)):
        product *= int(digit)
    return product

# Test
test_numbers = [123, 456, 99, 2024, 105]
for num in test_numbers:
    print(f"Product of digits of {num}: {product_of_digits(num)}")
