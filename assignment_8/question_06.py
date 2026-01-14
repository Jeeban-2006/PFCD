# Question 6
# Write a Python program that lets an instructor enter a student's first and last name 
# (strings) and three exam grades (integers). Save each student's data in a grades.csv 
# file using the csv module, with each record in the format:
# firstname,lastname,exam1grade,exam2grade,exam3grade

import csv

def add_student_data():
    print("Student Grade Entry System")
    print("="*60)
    
    # Open CSV file in append mode
    with open('grades.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        
        # Check if file is empty to add header
        file.seek(0, 2)  # Move to end of file
        if file.tell() == 0:  # If file is empty
            writer.writerow(['FirstName', 'LastName', 'Exam1', 'Exam2', 'Exam3'])
        
        while True:
            print("\nEnter student information (or 'quit' to exit):")
            
            first_name = input("First name: ").strip()
            if first_name.lower() == 'quit':
                break
            
            last_name = input("Last name: ").strip()
            
            try:
                exam1 = int(input("Exam 1 grade: "))
                exam2 = int(input("Exam 2 grade: "))
                exam3 = int(input("Exam 3 grade: "))
                
                # Write to CSV
                writer.writerow([first_name, last_name, exam1, exam2, exam3])
                print(f"✓ Data saved for {first_name} {last_name}")
                
            except ValueError:
                print("✗ Invalid grade entered. Please enter integers only.")
    
    print("\n" + "="*60)
    print("All student data saved to grades.csv")
    
    # Display saved data
    print("\nSaved Data:")
    print("-"*60)
    with open('grades.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(','.join(row))

# Run the program
add_student_data()
