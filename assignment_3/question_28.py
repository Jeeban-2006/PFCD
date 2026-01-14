# Question 28
# Write a function that takes a string of lowercase alphabets as inputs and gives an output by shifting them by one letter ahead. 
# Note that if the string has 'z', then it will be treated as 'a'. 
# Example: python → qzuipo, pythonabc → qzuipobcd.

def shift_letters(s):
    result = []
    for char in s:
        if char.isalpha():
            if char == 'z':
                result.append('a')
            elif char == 'Z':
                result.append('A')
            else:
                result.append(chr(ord(char) + 1))
        else:
            result.append(char)
    return ''.join(result)

# Test
test_strings = ["python", "pythonabc", "xyz", "hello"]
for test in test_strings:
    print(f"{test} → {shift_letters(test)}")
