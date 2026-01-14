# Question 26
# Write a function that replaces all vowels in a string with the character "*".

def replace_vowels(s):
    vowels = "aeiouAEIOU"
    return ''.join('*' if char in vowels else char for char in s)

# Test
test_strings = ["Hello World", "Python Programming", "Education"]
for test in test_strings:
    print(f"Original: '{test}'")
    print(f"Replaced: '{replace_vowels(test)}'")
