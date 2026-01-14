# Question 16
# Write a function to implement a basic calculator that can add, subtract, multiply, and divide two numbers based on user input.

def calculator(num1, num2, operation):
    if operation == '+' or operation == 'add':
        return num1 + num2
    elif operation == '-' or operation == 'subtract':
        return num1 - num2
    elif operation == '*' or operation == 'multiply':
        return num1 * num2
    elif operation == '/' or operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operation"

# Test
print(f"10 + 5 = {calculator(10, 5, '+')}")
print(f"10 - 5 = {calculator(10, 5, '-')}")
print(f"10 * 5 = {calculator(10, 5, '*')}")
print(f"10 / 5 = {calculator(10, 5, '/')}")
