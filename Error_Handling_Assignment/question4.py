#!usr/bin/python3
user_input = input("Enter a number: ")

try:
    # Attempt to convert the input to an integer
    converted_number = int(user_input)
    print("The number you entered is:", converted_number)

except ValueError:
    # Handle the case where the input is not a valid integer
    print("Error: Please enter a valid integer.")
