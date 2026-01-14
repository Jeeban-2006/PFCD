# Question 14
# Write a function to determine if a given number is an Armstrong number. 
# (An Armstrong number is a number that is equal to the sum of its digits, each raised to the power of the number of digits, 
# e.g., 153 = 1³ + 5³ + 3³, 1634 = 1⁴ + 6⁴ + 3⁴ + 4⁴).

def is_armstrong_number(number):
    num_str = str(number)
    num_digits = len(num_str)
    
    total = sum(int(digit) ** num_digits for digit in num_str)
    
    return total == number

# Test
test_numbers = [153, 1634, 123, 9474, 370]
for num in test_numbers:
    result = is_armstrong_number(num)
    print(f"{num} is {'an' if result else 'not an'} Armstrong number")
