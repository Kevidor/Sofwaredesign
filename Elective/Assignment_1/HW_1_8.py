"""
Name: Holzmann Kevin
Date: 26 Nov 2024

Define a function which can generate a list where the values are square of numbers be-
tween 1 and 20 (both included). Then the function needs to print the last 5 elements in
the list.
"""

def squares_to_20():
    squares = [x**2 for x in range(1, 21)]
    print(squares[-6:-1])

squares_to_20()