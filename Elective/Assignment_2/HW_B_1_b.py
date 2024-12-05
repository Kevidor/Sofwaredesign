"""
Name: Holzmann Kevin
Date: 1 Dez 2024

Assigment:
Write a Python program to create a class that represents a shape.
Include methods to calculate its area and perimeter. Implement subclasses for different shapes like circle, triangle, and square.
"""

import math
from abc import ABC, abstractmethod

class Shape(ABC):
    #implementieren Sie die Klasse fertig
    @abstractmethod
    def calc_Area(self):
        pass
    @abstractmethod
    def calc_Perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, diameter: float) -> None:
        self.diameter = diameter
        self.radius = diameter/2
    
    def calc_Area(self):
        return self.radius**2 * math.pi

    def calc_Perimeter(self):
        return self.radius * 2 * math.pi
    
class Triangle(Shape):
    def __init__(self, side_a: float, side_b: float, side_c: float) -> None:
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.s = (side_a+side_b+side_c)/2
    
    def calc_Area(self) -> float:
        return math.sqrt(self.s * (self.s - self.side_a) * (self.s - self.side_b) * (self.s - self.side_c))

    def calc_Perimeter(self) -> float:
        return self.s * 2
    
class Square(Shape):
    def __init__(self, side: float) -> None:
        self.side = side
    
    def calc_Area(self) -> float:
        return self.side**2

    def calc_Perimeter(self) -> float:
        return self.side * 4