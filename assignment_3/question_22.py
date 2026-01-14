# Question 22
# Create a function that prints the first 10 terms of an arithmetic progression.

def arithmetic_progression(first_term, common_diff, n=10):
    ap_terms = []
    for i in range(n):
        term = first_term + i * common_diff
        ap_terms.append(term)
    return ap_terms

# Test
print("AP with first term = 2, common difference = 3:")
print(arithmetic_progression(2, 3))
print("\nAP with first term = 5, common difference = 5:")
print(arithmetic_progression(5, 5))
