import math

# Base class
class Shape:
    def area(self):
        return 0

# Rectangle subclass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Circle subclass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# 🧑‍💻 Get user input
shape_type = input("Choose a shape (rectangle or circle): ").strip().lower()

try:
    if shape_type == "rectangle":
        width = float(input("Enter the width: "))
        height = float(input("Enter the height: "))
        rect = Rectangle(width, height)
        print(f"Area of the rectangle: {rect.area():.2f}")

    elif shape_type == "circle":
        radius = float(input("Enter the radius: "))
        circ = Circle(radius)
        print(f"Area of the circle: {circ.area():.2f}")

    else:
        print("Invalid shape selected.")

except ValueError:
    print("Error: Please enter valid numeric values.")
