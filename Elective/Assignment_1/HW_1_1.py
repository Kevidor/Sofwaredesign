"""
Name: Holzmann Kevin
Date: 26 Nov 2024

Assigment:
Write a program which will find all such numbers which are divisible by 11 but are not a
multiple of 23, between 2000 and 3200 (both included). The numbers obtained should be
printed in a comma-separated sequence on a single line.
"""

suit_nums = []
# iterates through range and checks each iteration if the contitions are met
# if true appends it to suit_num (suitable numbers)
for num in range(2000, 3201):
    if (num % 11 == 0 and not num % 23 == 0):
        suit_nums.append(num)

print(suit_nums)