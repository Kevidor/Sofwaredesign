"""
Name: Holzmann Kevin
Date: 1 Dez 2024

Assigment:
Write a Python program that iterates the integers from 1 to 50.
For multiples of three, print "Fizz".
For multiples of five, print "Buzz".
For numbers that are multiples of both three and five, print "FizzBuzz".

Expected Output:

fizzbuzz  
1  
2  
fizz  
4  
buzz  
...  
"""

for i in range(51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)