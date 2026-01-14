# Question 27
# Write a function that takes a positive number as an input and converts the respective digits into corresponding text. 
# Example: 85 → eight five, 8512 → eight five one two

def digits_to_text(number):
    digit_names = {
        '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
        '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
    }
    
    return ' '.join(digit_names[digit] for digit in str(number))

# Test
test_numbers = [85, 8512, 123, 9876]
for num in test_numbers:
    print(f"{num} → {digits_to_text(num)}")
