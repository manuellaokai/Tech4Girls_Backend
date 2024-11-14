#!usr/bin/python3
try:
    # Attempt to convert the user input to an integer
    age = int(input("Enter your age: "))

    # Age validation
    if age < 0:
        print("Age cannot be negative!")
    elif age > 120:
        print("That age is unlikely!")
    else:
        print("Your age is:", age)

except ValueError:
    # Handle the case where the input is not a valid integer
    print("Error: Please enter a valid number for your age.")
