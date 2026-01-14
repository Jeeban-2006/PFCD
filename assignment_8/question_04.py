# Question 4
# What is the significance of file modes ('r', 'w', 'a', 'b') in Python?

print("Question 4: Significance of File Modes in Python")
print("="*70)

print("\nFILE MODES OVERVIEW:")
print("="*70)

print("\n1. 'r' - READ MODE:")
print("   - Opens file for reading (default mode)")
print("   - File must exist, otherwise FileNotFoundError")
print("   - File pointer at beginning")
print("   - Cannot write to file")

print("\n2. 'w' - WRITE MODE:")
print("   - Opens file for writing")
print("   - Creates new file if doesn't exist")
print("   - OVERWRITES existing file content")
print("   - File pointer at beginning")

print("\n3. 'a' - APPEND MODE:")
print("   - Opens file for writing")
print("   - Creates new file if doesn't exist")
print("   - Preserves existing content")
print("   - File pointer at end")
print("   - New data added at end")

print("\n4. 'b' - BINARY MODE:")
print("   - Used with other modes (rb, wb, ab)")
print("   - Reads/writes binary data (images, videos, etc.)")
print("   - No text encoding/decoding")
print("   - Returns/expects bytes instead of strings")

print("\n" + "="*70)
print("COMMON COMBINATIONS:")
print("="*70)
print("'r'  or 'rt' - Read text (default)")
print("'rb'         - Read binary")
print("'w'  or 'wt' - Write text (overwrite)")
print("'wb'         - Write binary (overwrite)")
print("'a'  or 'at' - Append text")
print("'ab'         - Append binary")
print("'r+'         - Read and write")
print("'w+'         - Write and read (overwrite)")
print("'a+'         - Append and read")

print("\n" + "="*70)
print("DEMONSTRATION:")
print("="*70)

# 'w' mode - Write (creates/overwrites)
print("\n1. Writing with 'w' mode:")
with open('demo.txt', 'w') as f:
    f.write("First line\n")
    f.write("Second line\n")
print("   File created with 2 lines")

# 'r' mode - Read
print("\n2. Reading with 'r' mode:")
with open('demo.txt', 'r') as f:
    content = f.read()
    print(f"   Content:\n   {repr(content)}")

# 'a' mode - Append
print("\n3. Appending with 'a' mode:")
with open('demo.txt', 'a') as f:
    f.write("Third line (appended)\n")
print("   Added third line")

# Read again
print("\n4. Reading updated file:")
with open('demo.txt', 'r') as f:
    content = f.read()
    print(f"   Content:\n   {repr(content)}")

# 'wb' mode - Write binary
print("\n5. Binary mode 'wb':")
with open('demo.bin', 'wb') as f:
    f.write(b'\x00\x01\x02\x03')
print("   Binary data written")

# 'rb' mode - Read binary
print("\n6. Binary mode 'rb':")
with open('demo.bin', 'rb') as f:
    data = f.read()
    print(f"   Binary data: {data}")

print("\n" + "="*70)
print("KEY POINTS:")
print("="*70)
print("• Always close files (use 'with' statement)")
print("• 'w' mode is destructive - use carefully")
print("• 'a' mode is safe for logging")
print("• 'b' mode for non-text files")
print("• Default is 'rt' (read text)")
