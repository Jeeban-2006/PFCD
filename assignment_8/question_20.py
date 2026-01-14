# Question 20
# Write a program to analyze the distribution of ticket prices in the Titanic dataset. 
# Using Pandas, filter and display the names of passengers who were under 18 years old 
# on the Titanic.

import pandas as pd

def analyze_titanic_data(csv_file):
    """
    Analyze Titanic dataset: ticket price distribution and passengers under 18.
    
    Args:
        csv_file: Path to Titanic CSV file
    """
    try:
        # Read CSV file
        df = pd.read_csv(csv_file)
        
        print(f"✓ Loaded Titanic dataset with {len(df)} passengers")
        print()
        
        # Ticket price distribution
        print("="*70)
        print("TICKET PRICE DISTRIBUTION:")
        print("="*70)
        print(df['Fare'].describe())
        print()
        
        # Passengers under 18
        print("="*70)
        print("PASSENGERS UNDER 18 YEARS OLD:")
        print("="*70)
        
        under_18 = df[df['Age'] < 18]
        
        if len(under_18) > 0:
            print(f"\nFound {len(under_18)} passenger(s) under 18:")
            print("-"*70)
            for idx, row in under_18.iterrows():
                print(f"Name: {row['Name']}")
                print(f"  Age: {row['Age']}")
                print(f"  Sex: {row['Sex']}")
                print(f"  Class: {row['Pclass']}")
                print(f"  Fare: ${row['Fare']:.2f}")
                print()
        else:
            print("No passengers under 18 found.")
        
        return df, under_18
    
    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found.")
        return None, None
    except Exception as e:
        print(f"Error: {e}")
        return None, None

# Create sample Titanic CSV file with more data
csv_content = """PassengerId,Survived,Pclass,Name,Sex,Age,Fare
1,1,1,"Allen, Miss. Elisabeth",female,29,211.3375
2,0,3,"Moran, Mr. James",male,25,7.925
3,1,2,"Brown, Mrs. Mary",female,35,51.8625
4,0,3,"Smith, Mr. John",male,40,8.05
5,1,1,"Clark, Miss. Martha",female,18,83.1583
6,0,3,"Williams, Mr. Charles",male,12,10.5
7,1,2,"Moore, Miss. Ann",female,16,30.0708
8,0,3,"Wilson, Mr. Henry",male,19,7.75"""

with open('titanic.csv', 'w') as f:
    f.write(csv_content)

print("Analyzing Titanic Dataset")
print("="*70)

# Analyze the data
df, under_18 = analyze_titanic_data('titanic.csv')
