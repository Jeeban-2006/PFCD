# Question 18
# Write a function to check if a string is an Anagram of another string. 
# (An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once, e.g., the marvelous cinema → i am lord voldemort)

def is_anagram(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    return sorted(str1) == sorted(str2)

# Test
test_pairs = [
    ("listen", "silent"),
    ("the marvelous cinema", "i am lord voldemort"),
    ("hello", "world")
]
for str1, str2 in test_pairs:
    print(f"'{str1}' and '{str2}' are anagrams: {is_anagram(str1, str2)}")
