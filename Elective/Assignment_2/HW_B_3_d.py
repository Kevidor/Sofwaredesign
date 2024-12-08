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
    """Searches the Keys of a dict by its value

    Args:
        a_dict (dict): The Dict to search in
        search_value (any): The value to search for

    Returns:
        list: The list of the keys found with that value
    """
    found_keys = []
    for key, value in a_dict.items():
        if value == search_value:
            found_keys.append(key)
    
    return found_keys

# Example of the search_keys_by_values Function
if __name__ == "__main__":  
    my_dict = {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}  

    print(search_keys_by_values(my_dict, 20))