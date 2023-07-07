#!/usr/bin/python3
"""add_integer"""


def add_integer(a, b=98):
    """
    Function that performs addition of two numbers.

    Returns :
        b casted to int in case a in None
        a added to b casted to int

    Raises :
        TypeError in case a is not an int nor a float
        TypeError in case b is not an int nor a float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
