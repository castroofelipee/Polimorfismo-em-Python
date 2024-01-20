import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


def print_area(shape):
    print(f"Área: {shape.area()}")


circle = Circle(radius=5)
rectangle = Rectangle(length=4, width=6)


print_area(circle)     
print_area(rectangle)   
