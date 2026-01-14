# Question 11
# Create a function that determines whether a string can be rearranged to form a palindrome.

def can_form_palindrome(s):
    from collections import Counter
    s = s.lower().replace(" ", "")
    char_count = Counter(s)
    
    odd_count = sum(1 for count in char_count.values() if count % 2 != 0)
    return odd_count <= 1

# Test
test_cases = ["racecar", "aabbcc", "hello", "aab"]
for test in test_cases:
    print(f"'{test}' can form palindrome: {can_form_palindrome(test)}")
