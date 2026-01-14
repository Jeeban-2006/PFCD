# Question 6
# Define a function to check if a given string is a palindrome. Example: madam ♡ madam, racecar ♡ racecar

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

# Test
test_cases = ["madam", "racecar", "hello", "A man a plan a canal Panama"]
for test in test_cases:
    print(f"'{test}' is palindrome: {is_palindrome(test)}")
