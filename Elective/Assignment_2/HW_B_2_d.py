"""
Name: Holzmann Kevin
Date: 1 Dez 2024

Assigment:
Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
Use the continue statement.

Expected Output:

0 1 2 4 5  
"""

# Iterates through range and continues with the loop if the number is either 3 or 6
for i in range(7):
    if i == 3 or i == 6:
        continue
    print(i, end=" ")
print("")