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

my_dict = {'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}

# Return the dict as a list of tuples
print(list(my_dict.items()))