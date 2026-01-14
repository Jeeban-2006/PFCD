# Question 17
# Create a function that takes a string and returns a new string where all the vowels are removed.

def remove_vowels(s):
    vowels = "aeiouAEIOU"
    return ''.join(char for char in s if char not in vowels)

# Test
test_strings = ["Hello World", "Python Programming", "aeiou"]
for test in test_strings:
    print(f"Original: '{test}' -> No vowels: '{remove_vowels(test)}'")
