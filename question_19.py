# Question 19
# Create a function to find the greatest common divisor (GCD) of two numbers using a while loop.

def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Test
test_pairs = [(48, 18), (56, 98), (100, 50)]
for num1, num2 in test_pairs:
    print(f"GCD of {num1} and {num2} is {find_gcd(num1, num2)}")
