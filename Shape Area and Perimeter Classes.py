import math


class Shape:
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def calculate_area(self):
        return round(self.length * self.length, 3)

    def calculate_perimeter(self):
        return round(4 * self.length, 3)


class Circle(Shape):
    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = diameter / 2

    def calculate_area(self):
        return round(math.pi * (self.radius * self.radius), 3)

    def calculate_perimeter(self):
        return round(2 * math.pi * self.radius, 3)

