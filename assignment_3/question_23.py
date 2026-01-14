# Question 23
# Write a function that returns the index of each vowel in a string using a for loop.

def find_vowel_indices(s):
    vowels = "aeiouAEIOU"
    indices = []
    for i in range(len(s)):
        if s[i] in vowels:
            indices.append((s[i], i))
    return indices

# Test
test_strings = ["Hello World", "Python", "Education"]
for test in test_strings:
    result = find_vowel_indices(test)
    print(f"Vowels in '{test}': {result}")
