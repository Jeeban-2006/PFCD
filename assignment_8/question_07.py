# Question 7
# Write a Python program that counts the number of words in a given text file.
#
# Input file, sample.txt contains:
# Python is a versatile programming language.
# It is widely used in data science, web development, and automation.
#
# Output: The file 'sample.txt' contains 16 words.

def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
        
        return word_count
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return 0
    except Exception as e:
        print(f"Error reading file: {e}")
        return 0

# Create sample file
with open('sample.txt', 'w') as f:
    f.write("Python is a versatile programming language.\n")
    f.write("It is widely used in data science, web development, and automation.\n")

# Count words
filename = 'sample.txt'
word_count = count_words_in_file(filename)

print(f"The file '{filename}' contains {word_count} words.")
