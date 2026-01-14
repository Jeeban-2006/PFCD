# Question 18
# Write a program to merge two CSV files containing Titanic data and print the 
# combined dataset.

import csv

def merge_csv_files(file1, file2, output_file):
    """
    Merge two CSV files and save to output file.
    
    Args:
        file1: First CSV file path
        file2: Second CSV file path
        output_file: Output CSV file path
    """
    try:
        # Read first CSV file
        with open(file1, 'r') as f:
            reader1 = csv.reader(f)
            data1 = list(reader1)
        
        # Read second CSV file
        with open(file2, 'r') as f:
            reader2 = csv.reader(f)
            data2 = list(reader2)
        
        # Check if headers match
        if data1[0] != data2[0]:
            print("Warning: CSV headers don't match!")
        
        # Merge data (skip header from second file)
        merged_data = data1 + data2[1:]
        
        # Write merged data to output file
        with open(output_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(merged_data)
        
        print(f"✓ Successfully merged {len(data1)-1} rows from '{file1}'")
        print(f"✓ and {len(data2)-1} rows from '{file2}'")
        print(f"✓ Total rows in merged file: {len(merged_data)-1}")
        print(f"✓ Saved to '{output_file}'")
        
        return merged_data
    
    except FileNotFoundError as e:
        print(f"Error: File not found - {e}")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []

# Create sample Titanic CSV files
csv1_content = """PassengerId,Survived,Pclass,Name,Sex,Age
1,1,1,"Allen, Miss. Elisabeth",female,29,211.3375
2,0,3,"Moran, Mr. James",male,25,7.925"""

csv2_content = """PassengerId,Survived,Pclass,Name,Sex,Age
3,1,2,"Brown, Mrs. Mary",female,35,51.8625
4,0,3,"Smith, Mr. John",male,40,8.05"""

with open('titanic1.csv', 'w') as f:
    f.write(csv1_content)

with open('titanic2.csv', 'w') as f:
    f.write(csv2_content)

print("Merging Titanic CSV Files")
print("="*60)

# Merge the files
merged_data = merge_csv_files('titanic1.csv', 'titanic2.csv', 'titanic_merged.csv')

# Display merged data
print("\nMerged Dataset:")
print("-"*60)
for row in merged_data:
    print(','.join(row))
