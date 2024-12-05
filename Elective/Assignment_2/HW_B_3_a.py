"""
Name: Holzmann Kevin
Date: 1 Dez 2024

Assigment:
Write a Python program to find the key of the maximum value in a dictionary.

Expected Output:

{'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}  
Finds the key of the maximum and minimum value of the said dictionary:  
('Roxanne', 'Theodore') 
"""

people_dict = {'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}

print(f"{max(people_dict, key= people_dict.get)} {min(people_dict, key= people_dict.get)}")
