# Question 21
# Write a function to calculate the factorial of a number using a loop.

def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Test
test_numbers = [5, 0, 7, 10]
for num in test_numbers:
    print(f"{num}! = {factorial(num)}")
