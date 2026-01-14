# Question 15
# Create a function that returns the nth number in the Fibonacci sequence.

def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

# Test
for i in range(1, 11):
    print(f"Fibonacci({i}) = {fibonacci(i)}")
