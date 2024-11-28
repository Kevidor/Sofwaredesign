"""
Name: Holzmann Kevin
Date: 26 Nov 2024

Assigment:
Write a program, which will find all such numbers between 1000 and 3000 (both included)
such that each digit of the number is an even number. The numbers obtained should be
printed in a comma-separated sequence on a single line.
"""

output_text = []
for num in range(1000, 3001):
    if all(int(digit) % 2 == 0 for digit in str(num)):
        output_text.append(num)

print(output_text)