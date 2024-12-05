"""
Name: Holzmann Kevin
Date: 1 Dez 2024

Assigment:
Write a Python program to find all keys in a dictionary that have the given value.
Expected Output:

Original dictionary elements:  
{'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
Find all keys in the said dictionary that have the specified value:  
['Roxanne', 'Betty']
"""

def search_keys_by_values(a_dict: dict, search_value: any) -> list:
    found_keys = []
    for key, value in a_dict.items():
        if value == search_value:
            found_keys.append(key)
    
    return found_keys

my_dict = {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}  

print(search_keys_by_values(my_dict, 20))