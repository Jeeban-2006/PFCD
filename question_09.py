# Question 9
# Write two functions, one of which converts a binary number to decimal and the other one does the reverse.

def binary_to_decimal(binary):
    return int(str(binary), 2)

def decimal_to_binary(decimal):
    return bin(decimal)[2:]

# Test
binary_num = "1010"
decimal_num = 10

print(f"Binary {binary_num} to Decimal: {binary_to_decimal(binary_num)}")
print(f"Decimal {decimal_num} to Binary: {decimal_to_binary(decimal_num)}")
