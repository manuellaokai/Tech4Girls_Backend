#!usr/bin/python3
try:
    # Get input from the user
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    
    # Perform division
    result = numerator / denominator
    
    # Output the result
    print("The result is:", result)

except ValueError:
    print("Invalid input. Please enter valid integers.")

except ZeroDivisionError:
    print("Error: The denominator cannot be zero.")
