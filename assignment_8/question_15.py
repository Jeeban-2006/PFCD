# Question 15
# Write the output of the following program

print("Question 15: Output of File Operations Programs")
print("="*70)

print("\n(a) Program:")
print("-"*70)
print("""
f = open('PYTHON', 'w')
f.write('failure is a part of success')
f = open('PYTHON', 'r')
print(f.read(4))
f.close()
""")
print("\nOutput: 'fail'")
print("Explanation: Opens file in write mode, writes text, then reads first 4 chars")

print("\n" + "="*70)
print("\n(b) Program:")
print("-"*70)
print("""
f = open('PYTHON', 'w')
f.write('failure is a part of success')
f = open('PYTHON', 'r')
print(f.read())
f.close()
""")
print("\nOutput: 'failure is a part of success'")
print("Explanation: Writes text and reads entire file content")

print("\n" + "="*70)
print("\n(c) Program:")
print("-"*70)
print("""
f = open('PYTHON', 'w')
f.write('failure is a part of success also, i am fine')
f = open('PYTHON', 'r')
print(f.readline())
f.close()
""")
print("\nOutput: 'failure is a part of success also, i am fine'")
print("Explanation: File has one line, readline() reads entire line")

print("\n" + "="*70)
print("\n(d) Program:")
print("-"*70)
print("""
f = open('PYTHON', 'w')
description = ['we either choose the pain of discipline', 'or', 'the pain of regrets']
f.writelines(description)
f = open('PYTHON', 'r')
print(f.read())
f.close()
""")
print("\nOutput: 'we either choose the pain of disciplineorthe pain of regrets'")
print("Explanation: writelines() doesn't add newlines between strings")

print("\n" + "="*70)
print("LIVE DEMONSTRATION:")
print("="*70)

# (a)
print("\n(a) Demonstration:")
f = open('PYTHON', 'w')
f.write('failure is a part of success')
f = open('PYTHON', 'r')
print(f"Output: '{f.read(4)}'")
f.close()

# (b)
print("\n(b) Demonstration:")
f = open('PYTHON', 'w')
f.write('failure is a part of success')
f = open('PYTHON', 'r')
print(f"Output: '{f.read()}'")
f.close()

# (c)
print("\n(c) Demonstration:")
f = open('PYTHON', 'w')
f.write('failure is a part of success also, i am fine')
f = open('PYTHON', 'r')
print(f"Output: '{f.readline()}'")
f.close()

# (d)
print("\n(d) Demonstration:")
f = open('PYTHON', 'w')
description = ['we either choose the pain of discipline', 'or', 'the pain of regrets']
f.writelines(description)
f = open('PYTHON', 'r')
print(f"Output: '{f.read()}'")
f.close()
