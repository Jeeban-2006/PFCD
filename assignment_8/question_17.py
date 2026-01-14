# Question 17
# Create a robust program to read user input and write it into a file, handling 
# invalid inputs gracefully.

def write_user_input_to_file():
    """
    Read user input and write to file with error handling.
    """
    filename = None
    
    try:
        # Get filename from user
        filename = input("Enter filename to save (e.g., output.txt): ").strip()
        
        if not filename:
            print("Error: Filename cannot be empty.")
            return
        
        # Get content from user
        print("\nEnter text to save (press Ctrl+Z then Enter on Windows, or Ctrl+D on Unix to finish):")
        print("-"*60)
        
        lines = []
        try:
            while True:
                line = input()
                lines.append(line)
        except EOFError:
            pass  # User finished input
        
        content = '\n'.join(lines)
        
        if not content.strip():
            print("Warning: No content entered.")
            return
        
        # Write to file
        with open(filename, 'w') as file:
            file.write(content)
        
        print(f"\n✓ Successfully wrote {len(lines)} line(s) to '{filename}'")
        print(f"✓ Total characters: {len(content)}")
        
    except PermissionError:
        print(f"Error: Permission denied to write to '{filename}'")
    except IOError as e:
        print(f"Error: Unable to write to file - {e}")
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Run the program
print("User Input to File Writer")
print("="*60)
write_user_input_to_file()
