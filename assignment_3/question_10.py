# Question 10
# Create a function that returns all the unique permutations of a given string.

from itertools import permutations

def get_permutations(s):
    perm_list = [''.join(p) for p in permutations(s)]
    return list(set(perm_list))

# Test
test_string = "abc"
result = get_permutations(test_string)
print(f"Permutations of '{test_string}': {sorted(result)}")
