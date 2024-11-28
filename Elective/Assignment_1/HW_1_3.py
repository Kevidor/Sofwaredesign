"""
Name: Holzmann Kevin
Date: 26 Nov 2024

Assigment:
Write a program that accepts a sequence of whitespace separated words as input and
prints the words after removing all duplicate words and sorting them alphanumerically.

Example Input: hello world and practice makes perfect and hello world again
Example Output: again and hello makes perfect practice world
"""

input_text = input("Enter equence of whitespace separated words: ")
input_text = input_text.split(" ")
output_text = []
for word in input_text:
    if word in output_text:
        continue
    else:
        output_text.append(word)
output_text.sort()
print(output_text)