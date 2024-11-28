"""
Name: Holzmann Kevin
Date: 26 Nov 2024

Write a program that accepts a sentence and calculate the number of letters and digits.

Example Input: hello world! 123
Example Output: LETTERS 10, DIGITS 3
"""

letters, digits = 0, 0
text = input("Enter a sentence: ")
for symbol in text:
    if str(symbol).isalpha():
        letters += 1
    elif str(symbol).isdigit():
        digits += 1
    else:
        continue
print(f"LETTERS {letters}, DIGITS {digits}")