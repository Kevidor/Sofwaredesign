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
    """
    Abstract base class for all shapes.
    Defines the interface for calculating area and perimeter.
    """

    @abstractmethod
    def calc_Area(self):
        """
        Abstract method to calculate the area of the shape.
        Must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def calc_Perimeter(self):
        """
        Abstract method to calculate the perimeter of the shape.
        Must be implemented by subclasses.
        """
        pass


class Circle(Shape):
    """
    Class representing a circle. Inherits from Shape.
    """

    def __init__(self, diameter: float) -> None:
        """
        Initializes a Circle instance.

        Args:
            diameter (float): Diameter of the circle.
        """
        self.diameter = diameter
        self.radius = diameter / 2

    def calc_Area(self) -> float:
        """
        Calculates the area of the circle using the formula πr².

        Returns:
            float: Area of the circle.
        """
        return self.radius ** 2 * math.pi

    def calc_Perimeter(self) -> float:
        """
        Calculates the perimeter (circumference) of the circle using the formula 2πr.

        Returns:
            float: Perimeter of the circle.
        """
        return self.radius * 2 * math.pi


class Triangle(Shape):
    """
    Class representing a triangle. Inherits from Shape.
    """

    def __init__(self, side_a: float, side_b: float, side_c: float) -> None:
        """
        Initializes a Triangle instance.

        Args:
            side_a (float): Length of side a.
            side_b (float): Length of side b.
            side_c (float): Length of side c.
        """
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.s = (side_a + side_b + side_c) / 2  # Semi-perimeter for area calculation.

    def calc_Area(self) -> float:
        """
        Calculates the area of the triangle using Heron's formula:
        Area = √(s * (s - a) * (s - b) * (s - c))

        Returns:
            float: Area of the triangle.
        """
        return math.sqrt(
            self.s * (self.s - self.side_a) * (self.s - self.side_b) * (self.s - self.side_c)
        )

    def calc_Perimeter(self) -> float:
        """
        Calculates the perimeter of the triangle.

        Returns:
            float: Perimeter of the triangle.
        """
        return self.side_a + self.side_b + self.side_c


class Square(Shape):
    """
    Class representing a square. Inherits from Shape.
    """

    def __init__(self, side: float) -> None:
        """
        Initializes a Square instance.

        Args:
            side (float): Length of one side of the square.
        """
        self.side = side

    def calc_Area(self) -> float:
        """
        Calculates the area of the square using the formula side².

        Returns:
            float: Area of the square.
        """
        return self.side ** 2

    def calc_Perimeter(self) -> float:
        """
        Calculates the perimeter of the square using the formula 4 * side.

        Returns:
            float: Perimeter of the square.
        """
        return self.side * 4

# Example of using the diffrent Shape classes
if __name__ == "__main__":
    # Creating all shapes
    square = Square(2)
    triangle = Triangle(3, 4, 5)
    circle = Circle(3)

    # Printing out there Area and Perimeter
    print(f"Square has Area: {square.calc_Area()} and Perimeter: {square.calc_Perimeter()}")
    print(f"Triangle has Area: {triangle.calc_Area()} and Perimeter: {triangle.calc_Perimeter()}")
    print(f"Circle has Area: {circle.calc_Area()} and Perimeter: {circle.calc_Perimeter()}")