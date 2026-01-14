# Question 14
# What will be the output produced on executing function inverse1 when the following 
# input is entered as the value of variable num:
# (a)5  (b)0  (c)2.0  (d)x  (e)None

def inverse1():
    """
    Function that demonstrates various exception handling scenarios.
    """
    try:
        num = input("Enter the number: ")
        num = float(num)
        inverse = 1.0 / num
        print(f"Inverse: {inverse}")
    except ValueError:
        print("ValueError: Invalid input, not a number.")
    except TypeError:
        print("TypeError: Invalid type for operation.")
    except ZeroDivisionError:
        print("ZeroDivisionError: Division by zero is not allowed.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        print("Function inverse completed")

print("Question 14: Output Analysis for inverse1()")
print("="*70)

print("\nANALYSIS OF DIFFERENT INPUTS:")
print("="*70)

print("\n(a) Input: 5")
print("-"*70)
print("Expected Output:")
print("   Enter the number: 5")
print("   Inverse: 0.2")
print("   Function inverse completed")

print("\n(b) Input: 0")
print("-"*70)
print("Expected Output:")
print("   Enter the number: 0")
print("   ZeroDivisionError: Division by zero is not allowed.")
print("   Function inverse completed")

print("\n(c) Input: 2.0")
print("-"*70)
print("Expected Output:")
print("   Enter the number: 2.0")
print("   Inverse: 0.5")
print("   Function inverse completed")

print("\n(d) Input: x")
print("-"*70)
print("Expected Output:")
print("   Enter the number: x")
print("   ValueError: Invalid input, not a number.")
print("   Function inverse completed")

print("\n(e) Input: None (user presses Enter without typing)")
print("-"*70)
print("Expected Output:")
print("   Enter the number: ")
print("   ValueError: Invalid input, not a number.")
print("   Function inverse completed")

print("\n" + "="*70)
print("LIVE DEMONSTRATION:")
print("="*70)
inverse1()
