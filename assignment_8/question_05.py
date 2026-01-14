# Question 5
# Write code that reads the grades from the grades.txt file. Display the individual 
# grades and their total, count, and average.

# First, create a sample grades.txt file
with open('grades.txt', 'w') as f:
    f.write("85\n90\n78\n92\n88\n76\n95\n82\n")

print("Reading grades from grades.txt file")
print("="*60)

# Read grades from file
grades = []
with open('grades.txt', 'r') as f:
    for line in f:
        grade = int(line.strip())
        grades.append(grade)

# Display individual grades
print("\nIndividual Grades:")
print("-" * 60)
for i, grade in enumerate(grades, 1):
    print(f"Grade {i}: {grade}")

# Calculate statistics
total = sum(grades)
count = len(grades)
average = total / count if count > 0 else 0

# Display statistics
print("\n" + "="*60)
print("STATISTICS:")
print("="*60)
print(f"Total:   {total}")
print(f"Count:   {count}")
print(f"Average: {average:.2f}")
