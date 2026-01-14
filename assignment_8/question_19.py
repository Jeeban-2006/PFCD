# Question 19
# Implement a program that reads a titanic1.CSV file into a Pandas DataFrame and 
# finds the passenger with the longest name.

import pandas as pd

def find_longest_name(csv_file):
    """
    Read CSV file and find passenger with longest name.
    
    Args:
        csv_file: Path to CSV file
    
    Returns:
        Series: Row data for passenger with longest name
    """
    try:
        # Read CSV file into DataFrame
        df = pd.read_csv(csv_file)
        
        print(f"✓ Successfully loaded {len(df)} passengers from '{csv_file}'")
        print()
        
        # Add column for name length
        df['NameLength'] = df['Name'].str.len()
        
        # Find passenger with longest name
        longest_name_idx = df['NameLength'].idxmax()
        longest_name_passenger = df.loc[longest_name_idx]
        
        return longest_name_passenger, df
    
    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found.")
        return None, None
    except Exception as e:
        print(f"Error: {e}")
        return None, None

# Create sample Titanic CSV file
csv_content = """PassengerId,Survived,Pclass,Name,Sex,Age
1,1,1,"Allen, Miss. Elisabeth Walton",female,29
2,0,3,"Moran, Mr. James",male,25
3,1,2,"Brown, Mrs. Mary Elizabeth Catherine",female,35
4,0,3,"Smith, Mr. John",male,40"""

with open('titanic1.csv', 'w') as f:
    f.write(csv_content)

print("Finding Passenger with Longest Name")
print("="*60)

# Find longest name
longest_passenger, df = find_longest_name('titanic1.csv')

if longest_passenger is not None:
    print("Passenger with the longest name:")
    print("-"*60)
    print(f"Name: {longest_passenger['Name']}")
    print(f"Name Length: {longest_passenger['NameLength']} characters")
    print(f"Passenger ID: {longest_passenger['PassengerId']}")
    print(f"Age: {longest_passenger['Age']}")
    print(f"Sex: {longest_passenger['Sex']}")
    print(f"Class: {longest_passenger['Pclass']}")
