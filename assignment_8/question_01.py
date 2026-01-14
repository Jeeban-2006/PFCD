# Question 1
# How does the read method differ from the readlines method?

print("Question 1: Difference between read() and readlines()")
print("="*70)

# Create a sample file for demonstration
with open('sample_demo.txt', 'w') as f:
    f.write("Line 1: Hello World\n")
    f.write("Line 2: Python Programming\n")
    f.write("Line 3: File Operations\n")

print("\n1. Using read() method:")
print("-" * 50)
with open('sample_demo.txt', 'r') as f:
    content = f.read()
    print(f"Type: {type(content)}")
    print(f"Content:\n{repr(content)}")

print("\n2. Using readlines() method:")
print("-" * 50)
with open('sample_demo.txt', 'r') as f:
    lines = f.readlines()
    print(f"Type: {type(lines)}")
    print(f"Content: {lines}")

print("\n" + "="*70)
print("KEY DIFFERENCES:")
print("="*70)
print("read():")
print("  - Reads entire file as a single string")
print("  - Returns: str")
print("  - Includes newline characters (\\n)")
print("  - Usage: When you need the whole file as one text block")
print()
print("readlines():")
print("  - Reads entire file and splits by lines")
print("  - Returns: list of strings")
print("  - Each element is a line (with \\n at end)")
print("  - Usage: When you need to process file line by line")
