#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """
    Calculates the minimum number of operations required
    to reduce a given number to 1.
    Parameters:
        n (int): The number to be reduced.
    Returns:
        int: The minimum number of operations required.
    """
    if n <= 1 or n is None or type(n) is not int:
        return 0
    operations = 0
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n -= 1
        operations += 1
    return operations
