"""
Name: Holzmann Kevin
Date: 1 Dez 2024

Assigment:
Write a Python program to create a flat list of all the values in a flat dictionary.
Expected Output:

{'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}  
Create a flat list of all the values of the said flat dictionary:  
[19, 20, 21, 20]  
"""

people_dict = {'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}

# Prints out all the values of the dict
print(list(people_dict.values()))