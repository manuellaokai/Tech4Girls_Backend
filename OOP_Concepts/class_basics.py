#!usr/bin/python3
class Car:
    # Initializer method (__init__) to set up the instance variables
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # Method to display the car's details
    def display_info(self):
        print(f"Car Details: {self.year} {self.make} {self.model}")

# Create an instance of the Car class
my_car = Car("Toyota", "Camry", 2020)

# Call the display_info method to print the car's details
my_car.display_info()