"""
Name: Holzmann Kevin
Date: 26 Nov 2024

Assigment:
Write a program which accepts a sequence of comma separated 4 digit binary numbers
as its input and then check whether they are divisible by 5 or not. The numbers that are
divisible by 5 are to be printed in a comma separated sequence.

Example Input: 0100,0011,1010,1001
Example Output: 1010
"""

input_binary = input("Enter a sequence of comma separated 4 digit binary numbers: ")
input_binary = input_binary.split(",")
output_binary =  []
for binary in input_binary:
    # Converts the binary to a decimal and then checks if it's divdeable by 5
    if int(binary, 2) % 5 == 0:
        output_binary.append(binary)
print(output_binary)

