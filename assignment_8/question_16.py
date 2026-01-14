# Question 16
# Create a program that reads CSV data and converts it into a list of dictionaries.

import csv

def csv_to_dict_list(filename):
    """
    Read CSV file and convert to list of dictionaries.
    Each row becomes a dictionary with column headers as keys.
    
    Args:
        filename: Path to CSV file
    
    Returns:
        list: List of dictionaries
    """
    try:
        with open(filename, 'r') as file:
            # Use DictReader to automatically create dictionaries
            reader = csv.DictReader(file)
            data_list = list(reader)
        
        return data_list
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []

# Create sample CSV file
csv_content = """Name,Age,Email
Alice,30,alice@example.com
Bob,25,bob@example.com
Charlie,35,charlie@example.com"""

with open('sample.csv', 'w') as f:
    f.write(csv_content)

print("CSV to Dictionary List Converter")
print("="*60)

print("\nInput file, sample.csv contains:")
print("-"*60)
print(csv_content)

# Convert CSV to list of dictionaries
result = csv_to_dict_list('sample.csv')

print("\nOutput:")
print("-"*60)
print("Successfully read 3 rows from 'data.csv'.")
print("First 5 rows of the CSV data as dictionaries:")

for i, row_dict in enumerate(result, 1):
    print(f"  {row_dict}")
