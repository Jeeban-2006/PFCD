# Question 11
# Write a Python function that takes two files of equal size as input from the user. 
# The first file contains weights of items and the second file contains corresponding 
# prices. Create another file that should contain price per unit weight for each item.

def calculate_price_per_unit():
    """
    Read weights and prices from two files, calculate price per unit weight,
    and save results to a new file.
    """
    try:
        # Read weights from first file
        with open('weights.txt', 'r') as f:
            weights = [float(line.strip()) for line in f]
        
        # Read prices from second file
        with open('prices.txt', 'r') as f:
            prices = [float(line.strip()) for line in f]
        
        # Check if both files have equal length
        if len(weights) != len(prices):
            print("Error: Files must have equal number of entries.")
            return
        
        # Calculate price per unit weight and write to output file
        with open('price_per_unit.txt', 'w') as f:
            print("\nPrice Per Unit Weight:")
            print("="*60)
            print(f"{'Item':<8} {'Weight':<10} {'Price':<10} {'Price/Unit'}")
            print("-"*60)
            
            for i, (weight, price) in enumerate(zip(weights, prices), 1):
                if weight == 0:
                    print(f"Item {i}: Cannot calculate (weight is zero)")
                    f.write(f"Item {i}: N/A (zero weight)\n")
                else:
                    price_per_unit = price / weight
                    print(f"Item {i:<3} {weight:<10.2f} {price:<10.2f} {price_per_unit:.2f}")
                    f.write(f"{price_per_unit:.2f}\n")
        
        print("\n✓ Results saved to 'price_per_unit.txt'")
    
    except FileNotFoundError as e:
        print(f"Error: File not found - {e}")
    except ValueError:
        print("Error: Invalid data in files. Please ensure all values are numbers.")
    except Exception as e:
        print(f"Error: {e}")

# Create sample files
with open('weights.txt', 'w') as f:
    f.write("2.5\n5.0\n1.2\n3.8\n")

with open('prices.txt', 'w') as f:
    f.write("50.0\n120.0\n36.0\n95.0\n")

# Run the function
calculate_price_per_unit()
