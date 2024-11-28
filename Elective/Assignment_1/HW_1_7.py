"""
Name: Holzmann Kevin
Date: 26 Nov 2024

Write a program that accepts a sentence and calculate the number of upper case letters
and lower case letters.

Example Input: Hello world!
Example Output:UPPER CASE 1, LOWER CASE 9
"""

upper_case, lower_case = 0, 0
text = input("Enter a sentence: ")
for symbol in text:
    if str(symbol).isupper():
        upper_case += 1
    elif str(symbol).islower():
        lower_case += 1
    else:
        continue
print(f"UPPER CASE {upper_case}, LOWER CASE {lower_case}")