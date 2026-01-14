# Question 24
# Write a function that removes all punctuation from a string.

def remove_punctuation(s):
    import string
    return ''.join(char for char in s if char not in string.punctuation)

# Test
test_strings = [
    "Hello, World!",
    "Python programming; it's amazing!",
    "What?! Really?"
]
for test in test_strings:
    print(f"Original: '{test}'")
    print(f"No punctuation: '{remove_punctuation(test)}'")
    print()
