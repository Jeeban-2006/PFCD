# Question 29
# Write a function to check if a given number is a perfect number. 
# (A number is called a perfect number if it is equal to the sum of its real divisors, 
# e.g., 6=1+2+3, 28=1+2+4+7+14).

def is_perfect_number(n):
    if n <= 0:
        return False
    
    divisors_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i
    
    return divisors_sum == n

# Test
test_numbers = [6, 28, 12, 496, 8128, 100]
for num in test_numbers:
    print(f"{num} is {'a' if is_perfect_number(num) else 'not a'} perfect number")
