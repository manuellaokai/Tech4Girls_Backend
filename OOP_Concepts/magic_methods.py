#!usr/bin/python3
class Rectangle:
    # Initializer method to set up length and width
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Property method to calculate area
    @property
    def area(self):
        return self.length * self.width

    # Property method to calculate perimeter
    @property
    def perimeter(self):
        return 2 * (self.length + self.width)

    # Dunder method __str__ to return string representation of the rectangle
    def __str__(self):
        return f"Rectangle(Length: {self.length}, Width: {self.width})"

    # Dunder method __eq__ to compare two rectangles based on area
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area == other.area
        return False


# Demonstrating the usage of the Rectangle class

# Create two rectangle instances with different dimensions
rectangle1 = Rectangle(6, 2)
rectangle2 = Rectangle(10, 5)

# Display the rectangles using the __str__ method
print(rectangle1)  # Output: Rectangle(Length: 6, Width: 2)
print(rectangle2)  # Output: Rectangle(Length: 10, Width: 5)

# Display the area and perimeter using the property methods
print(f"Area of rectangle1: {rectangle1.area}")  # Output: 15
print(f"Perimeter of rectangle1: {rectangle1.perimeter}")  # Output: 16

print(f"Area of rectangle2: {rectangle2.area}")  # Output: 12
print(f"Perimeter of rectangle2: {rectangle2.perimeter}")  # Output: 16

# Compare if the areas of the two rectangles are equal using the __eq__ method
print(f"Are the areas of rectangle1 and rectangle2 equal? {rectangle1 == rectangle2}")  
# Output: False