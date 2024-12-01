"""
Name: Holzmann Kevin
Date: 26 Nov 2024

Assigment:
Write a program that accepts a comma separated sequence of words as input and prints
the words in a comma-separated sequence after sorting them alphabetically.

Example Input: hello,bag,world
Example Output: bag,hello,world
"""

input_text = input("Enter a comma separated sequence of words: ")
input_text = input_text.split(",") # Splits text at each komma (,) and appends elements in a list
input_text.sort() # Sorts a list alphabetically
print(input_text)