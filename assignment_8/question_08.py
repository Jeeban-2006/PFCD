# Question 8
# Write a function to safely deserialize JSON data from a file and handle errors if 
# the data is invalid.

import json

def safely_deserialize_json(filename):
    """
    Safely deserialize JSON data from a file with error handling.
    
    Args:
        filename: Path to the JSON file
    
    Returns:
        tuple: (success: bool, data: dict/None, error_message: str/None)
    """
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        
        print(f"✓ JSON data successfully loaded from '{filename}'")
        return True, data, None
    
    except FileNotFoundError:
        error_msg = f"Error: The file '{filename}' does not exist."
        print(error_msg)
        return False, None, error_msg
    
    except json.JSONDecodeError as e:
        error_msg = f"Error: Invalid JSON format - {e}"
        print(error_msg)
        return False, None, error_msg
    
    except PermissionError:
        error_msg = f"Error: Permission denied to read '{filename}'"
        print(error_msg)
        return False, None, error_msg
    
    except Exception as e:
        error_msg = f"Unexpected error: {e}"
        print(error_msg)
        return False, None, error_msg

# Test the function
print("Testing Safe JSON Deserialization")
print("="*60)

# Test 1: Valid JSON file
print("\nTest 1: Valid JSON file")
print("-"*60)
valid_data = {
    "name": "Alice",
    "age": 30,
    "skills": ["Python", "Data Science"]
}
with open('data.json', 'w') as f:
    json.dump(valid_data, f, indent=2)

success, data, error = safely_deserialize_json('data.json')
if success:
    print("Deserialized Data:", data)

# Test 2: Invalid JSON file
print("\n\nTest 2: Invalid JSON file")
print("-"*60)
with open('invalid.json', 'w') as f:
    f.write('{"name": "Bob", "age": }')  # Invalid JSON

success, data, error = safely_deserialize_json('invalid.json')

# Test 3: Missing file
print("\n\nTest 3: Missing file")
print("-"*60)
success, data, error = safely_deserialize_json('missing.json')

print("\n" + "="*60)
print("No valid data could be loaded." if not success else "")
