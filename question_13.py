# Question 13
# Write a program that converts a Roman numeral to its integer equivalent.

def roman_to_integer(roman):
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    for char in reversed(roman):
        value = roman_values[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    
    return total

# Test
test_cases = ["III", "IV", "IX", "LVIII", "MCMXCIV"]
for roman in test_cases:
    print(f"{roman} = {roman_to_integer(roman)}")
