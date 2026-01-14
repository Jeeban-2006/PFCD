# Question 9
# Solve the problem of dividing two numbers, handling invalid inputs like zero or 
# non-numeric values.

def safe_division():
    """
    Safely divide two numbers with error handling for:
    - Non-numeric inputs
    - Division by zero
    - Other exceptions
    """
    try:
        # Get input from user
        num = input("Enter the numerator: ")
        num = float(num)
        
        denom = input("Enter the denominator: ")
        denom = float(denom)
        
        # Perform division
        result = num / denom
        
        print(f"\nResult: {num} / {denom} = {result}")
        return result
    
    except ValueError:
        print("Error: Invalid input. Please enter numeric values only.")
        return None
    
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

# Run the program
print("Safe Division Calculator")
print("="*60)
safe_division()
