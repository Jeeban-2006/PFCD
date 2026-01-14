# Question 7
# Write a Python function to check whether an alphabet is a vowel or consonant.

def check_vowel_consonant(char):
    if len(char) != 1 or not char.isalpha():
        return "Invalid input"
    
    vowels = "aeiouAEIOU"
    if char in vowels:
        return "Vowel"
    else:
        return "Consonant"

# Test
test_chars = ['a', 'b', 'e', 'z', 'A', 'M']
for char in test_chars:
    print(f"'{char}' is a {check_vowel_consonant(char)}")
