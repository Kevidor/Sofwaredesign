"""
Name: Holzmann Kevin
Date: 26 Nov 2024

A prime number is a number that can only be divided by itself and 1 without remainders.
Considering this definition please write a program which prints out the nth prime number.

Example Input: 532
Example Output: The 532nd prime is: 3833
"""

def is_prime(number: int) -> bool:
    """Checks if the input umber is a prime number

    Args:
        number (int): number to check for

    Returns:
        bool: True if input is a prime number
    """
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def nth_prime(n: int) -> int:
    """Returns the nth prime number

    Args:
        n (int): target_prime_position

    Returns:
        int: nth prime number
    """
    count = 0
    num = 1
    while count < n:
        num += 1
        if is_prime(num):
            count += 1
    return num

n = int(input("Enter the value of n: "))
print(f"The {n}th prime number is: {nth_prime(n)}")