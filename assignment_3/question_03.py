# Question 3
# Write a Python function to add the squares of the even numbers between 1 and 50 (both included).

def sum_of_even_squares():
    total = 0
    for num in range(1, 51):
        if num % 2 == 0:
            total += num ** 2
    return total

# Test
result = sum_of_even_squares()
print(f"Sum of squares of even numbers between 1 and 50: {result}")
