"""
Name: Holzmann Kevin
Date: 26 Nov 2024

Define a class named Rectangle which can be constructed by a length and width. The
Rectangle class has a method which can compute the area.
"""

class Rectangle:
    def __init__(self, lenght: float, width: float) -> None:
        """Creates a Rectangle out of a given Parameter

        Args:
            lenght (float): Lenght of the Rectangle
            width (float): Width of the Rectangle
        """
        self.lenght = lenght
        self.width = width

    def calcArea(self) -> float:
        """Calculate the Area of the Rectangle

        Returns:
            float: Area of the Rectangle
        """
        return self.lenght * self. width
    
rectangle = Rectangle(10, 4)
print(rectangle.calcArea())