"""
Name: Holzmann Kevin
Date: 1 Dez 2024

Assigment:
Write a Python program to construct the following pattern using a nested loop:

Expected Output:

1
22
333
4444
55555
"""

# Solution with nested for-loop. Outer for-loop iterates through the numbers
# and the inner for-loop iterates to print it the desired amount
for i in range(1, 6):
    for _ in range(i):
        print(i, end="")
    print("")

# Solution with one for loop and clever chasting of variables
# Since the number is also the amount of times it should be printed, 
# the current number i gets casted into an string and multiplied by its numerical value
for i in range(1, 6):
    print(str(i) * i)