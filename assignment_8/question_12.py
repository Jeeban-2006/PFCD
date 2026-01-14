# Question 12
# Create a program to extract and save unique email addresses from a large text file.

import re

def extract_unique_emails(input_file, output_file):
    """
    Extract unique email addresses from a text file and save to another file.
    
    Args:
        input_file: Input text file containing emails
        output_file: Output file to save unique emails
    """
    try:
        # Read the input file
        with open(input_file, 'r') as f:
            content = f.read()
        
        # Regular expression pattern for email addresses
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        
        # Find all email addresses
        emails = re.findall(email_pattern, content)
        
        # Get unique emails (case-insensitive)
        unique_emails = sorted(set(email.lower() for email in emails))
        
        # Save to output file
        with open(output_file, 'w') as f:
            for email in unique_emails:
                f.write(f"{email}\n")
        
        print(f"Extracted {len(unique_emails)} unique email addresses")
        print(f"Saved to '{output_file}'")
        
        return unique_emails
    
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []

# Create sample input file
sample_text = """
Hello, contact me at example1@example.com for more info. You can also reach me at test_email@example.org
or example1@example.com. Spam emails: spam@spammer.com, info@spammer.com

For business: contact@company.com, spam@spammer.com
Test emails: test_email@example.org, admin@website.net
"""

with open('sample.txt', 'w') as f:
    f.write(sample_text)

print("Extracting Email Addresses")
print("="*60)

# Extract and save unique emails
unique_emails = extract_unique_emails('sample.txt', 'Output.txt')

# Display results
print("\nUnique Email Addresses:")
print("-"*60)
for email in unique_emails:
    print(email)
