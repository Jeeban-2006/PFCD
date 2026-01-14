# Question 10
# Write a Python function that reads a file file1 and displays the number of words 
# and the number of vowels in the file.

def count_words_and_vowels(filename):
    """
    Count the number of words and vowels in a file.
    
    Args:
        filename: Path to the text file
    
    Returns:
        tuple: (word_count, vowel_count)
    """
    try:
        with open(filename, 'r') as file:
            content = file.read()
        
        # Count words
        words = content.split()
        word_count = len(words)
        
        # Count vowels
        vowels = 'aeiouAEIOU'
        vowel_count = sum(1 for char in content if char in vowels)
        
        return word_count, vowel_count
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return 0, 0
    except Exception as e:
        print(f"Error: {e}")
        return 0, 0

# Create sample file
with open('file1.txt', 'w') as f:
    f.write("Python programming is fun and educational.\n")
    f.write("It helps in solving real-world problems.\n")

# Test the function
filename = 'file1.txt'
word_count, vowel_count = count_words_and_vowels(filename)

print(f"File Analysis: '{filename}'")
print("="*60)
print(f"Number of words: {word_count}")
print(f"Number of vowels: {vowel_count}")
