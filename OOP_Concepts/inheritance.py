#!usr/bin/python3
# employee_manager.py

# Parent class Employee
class Employee:
    # Initializer method to set up the name and position
    def __init__(self, name, position):
        self.name = name
        self.position = position

    # Method to display employee's details
    def get_details(self):
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")


# Child class Manager inherits from Employee
class Manager(Employee):
    # Initializer method to set up department, using super() to call the parent class's __init__
    def __init__(self, name, position, department):
        super().__init__(name, position)  # Calling parent class's __init__
        self.department = department

    # Overriding get_details() method to include department
    def get_details(self):
        super().get_details()  # Calling parent class's get_details()
        print(f"Department: {self.department}")


# Demonstrating the usage of both classes

# Creating an instance of Employee
employee = Employee("Manuella Okai", "Software Developer")
print("Employee Details:")
employee.get_details()

# Creating an instance of Manager
manager = Manager("Habiba", "Software Development Manager", "IT")
print("\nManager Details:")
manager.get_details()