"""
This design is open for extension (we can add new shapes without modifying existing code) 
but closed for modification (we don't need to change the AreaCalculator class to support new shapes).
"""

from abc import ABC, abstractmethod

# Good example (follows OCP)
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class AreaCalculator:
    def calculate_area(self, shapes):
        return sum(shape.area() for shape in shapes)

# Usage
calculator = AreaCalculator()
shapes = [Rectangle(5, 4), Circle(3)]
total_area = calculator.calculate_area(shapes)
print(f"Total area: {total_area}")
