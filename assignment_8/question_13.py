# Question 13
# Identify two exceptions that may be raised while executing the following statement:
# result = a + b

print("Question 13: Exceptions in 'result = a + b'")
print("="*70)

print("\nTWO MAIN EXCEPTIONS:")
print("="*70)

print("\n1. NameError:")
print("   - Raised when variable 'a' or 'b' is not defined")
print("   - Occurs before the addition operation")

print("\nExample:")
try:
    result = a + b  # a and b are not defined
except NameError as e:
    print(f"   NameError caught: {e}")

print("\n2. TypeError:")
print("   - Raised when operands have incompatible types")
print("   - Cannot add certain types together")

print("\nExample:")
try:
    a = "hello"
    b = 5
    result = a + b  # Can't add string and integer
except TypeError as e:
    print(f"   TypeError caught: {e}")

print("\n" + "="*70)
print("OTHER POSSIBLE EXCEPTIONS:")
print("="*70)

print("\n3. MemoryError (rare):")
print("   - If result is too large to fit in memory")

print("\n4. OverflowError (rare):")
print("   - For certain numeric operations that exceed limits")

print("\n" + "="*70)
print("DEMONSTRATION OF VARIOUS CASES:")
print("="*70)

test_cases = [
    ("Valid addition", 5, 10),
    ("String concatenation", "Hello ", "World"),
    ("Incompatible types", "5", 10),
    ("List concatenation", [1, 2], [3, 4])
]

for desc, val_a, val_b in test_cases:
    print(f"\n{desc}:")
    try:
        a = val_a
        b = val_b
        result = a + b
        print(f"   {a} + {b} = {result}")
    except TypeError as e:
        print(f"   TypeError: {e}")
