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
# Solution with nested for-loop
for i in range(1, 6):
    for _ in range(i):
        print(i, end="")
    print("")

# Solution with one for loop and clever chasting of variables
for i in range(1, 6):
    print(str(i) * i)