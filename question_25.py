# Question 25
# Write a function to check if two numbers are coprime.

def are_coprime(a, b):
    def gcd(x, y):
        while y != 0:
            x, y = y, x % y
        return x
    
    return gcd(a, b) == 1

# Test
test_pairs = [(8, 15), (14, 21), (17, 19), (12, 18)]
for num1, num2 in test_pairs:
    print(f"{num1} and {num2} are coprime: {are_coprime(num1, num2)}")
