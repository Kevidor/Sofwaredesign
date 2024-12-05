"""
Name: Holzmann Kevin
Date: 1 Dez 2024

Assigment:
Write a Python program to transform a dictionary into a list of tuples.
Expected Output:

Original Dictionary:  
{'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}  
Convert the said dictionary to a list of tuples:  
[('Red', 1), ('Green', 3), ('White', 5), ('Black', 2), ('Pink', 4)]  
"""

def dict_to_tuples(a_dict: dict) -> list[tuple]:
    list_of_tuples = []
    for key, value in my_dict.items():
        list_of_tuples.append((key, value))
    return list_of_tuples


my_dict = {'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}

print(dict_to_tuples(my_dict))