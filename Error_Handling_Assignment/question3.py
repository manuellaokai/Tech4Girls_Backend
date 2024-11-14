#!usr/bin/python3
user_input = input("Enter a number: ")

try:
    # Attempt to convert the input to an integer
    converted_number = int(user_input)
    print("The number you entered is:", converted_number)

except ValueError:
    # Handle the case where the input is not a valid integer
    print("Error: Please enter a valid integer.")



user_input = input("Enter a number: ")

try:
    # First, attempt to convert the input to a float, then to an integer
    converted_number = int(float(user_input))
    print("The number you entered is:", converted_number)

except ValueError:
    # Handle the case where the input is not a valid number
    print("Error: Please enter a valid number (integer or floating-point).")
