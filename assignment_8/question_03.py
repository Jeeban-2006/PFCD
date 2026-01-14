# Question 3
# Why is the pickle module considered a security risk in some cases?

import pickle

print("Question 3: Why is pickle module a security risk?")
print("="*70)

print("\nSECURITY RISKS OF PICKLE MODULE:")
print("-" * 70)

print("\n1. CODE EXECUTION VULNERABILITY:")
print("   - Pickle can execute arbitrary Python code during deserialization")
print("   - Malicious pickle data can run harmful commands")
print("   - Attacker can craft pickle data to execute system commands")

print("\n2. TRUST ISSUE:")
print("   - Never unpickle data from untrusted sources")
print("   - No built-in security mechanism to verify data source")
print("   - Can't validate pickle data before loading")

print("\n3. MALICIOUS PAYLOAD EXAMPLE (Conceptual):")
print("   - Attacker can create pickle with __reduce__ method")
print("   - This method can execute any function during unpickling")
print("   - Could delete files, steal data, install malware, etc.")

print("\n" + "="*70)
print("DEMONSTRATION (Safe Example):")
print("="*70)

# Safe pickle usage
data = {"name": "Alice", "scores": [85, 90, 78]}

# Serialize
with open('data.pkl', 'wb') as f:
    pickle.dump(data, f)
print("\nData pickled successfully (safe)")

# Deserialize
with open('data.pkl', 'rb') as f:
    loaded_data = pickle.load(f)
print(f"Loaded data: {loaded_data}")

print("\n" + "="*70)
print("SECURITY BEST PRACTICES:")
print("="*70)
print("✓ Only unpickle data from trusted sources")
print("✓ Use JSON instead for untrusted data")
print("✓ Validate and sanitize data before pickling")
print("✓ Use digital signatures to verify pickle integrity")
print("✓ Consider alternatives: JSON, MessagePack, Protocol Buffers")
print("✓ Implement access controls on pickle files")

print("\n" + "="*70)
print("WHEN TO USE PICKLE:")
print("="*70)
print("✓ Internal applications with trusted data")
print("✓ Caching computed results locally")
print("✓ Storing complex Python objects temporarily")
print("✓ Machine learning model serialization (with caution)")

print("\n" + "="*70)
print("WHEN NOT TO USE PICKLE:")
print("="*70)
print("✗ Data from external/untrusted sources")
print("✗ Data transmitted over network from unknown clients")
print("✗ User-uploaded files")
print("✗ Public-facing APIs")
