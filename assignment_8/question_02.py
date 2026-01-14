# Question 2
# What is the purpose of JSON serialization?

import json

print("Question 2: Purpose of JSON Serialization")
print("="*70)

print("\nJSON SERIALIZATION PURPOSE:")
print("-" * 70)
print("1. Convert Python objects to JSON format (string)")
print("2. Store data in a human-readable, platform-independent format")
print("3. Transfer data between systems and languages")
print("4. Save data to files or transmit over networks")
print("5. Enable data interchange in web APIs")

print("\n" + "="*70)
print("DEMONSTRATION:")
print("="*70)

# Python object
student = {
    "name": "John Doe",
    "age": 20,
    "grades": [85, 90, 78],
    "is_active": True,
    "address": {
        "city": "New York",
        "zip": "10001"
    }
}

print("\n1. Original Python Dictionary:")
print(student)
print(f"Type: {type(student)}")

# Serialization (Python object → JSON string)
json_string = json.dumps(student, indent=2)
print("\n2. After Serialization (JSON string):")
print(json_string)
print(f"Type: {type(json_string)}")

# Save to file
with open('student.json', 'w') as f:
    json.dump(student, f, indent=2)
print("\n3. Saved to 'student.json' file")

# Deserialization (JSON string → Python object)
loaded_data = json.loads(json_string)
print("\n4. After Deserialization (back to Python):")
print(loaded_data)
print(f"Type: {type(loaded_data)}")

print("\n" + "="*70)
print("KEY BENEFITS:")
print("="*70)
print("✓ Human-readable format")
print("✓ Language-independent (JavaScript, Python, Java, etc.)")
print("✓ Lightweight and fast")
print("✓ Built-in support in most programming languages")
print("✓ Perfect for configuration files and APIs")
