#!/usr/bin/python3
"""print_square function"""


def print_square(size):
    """
    Function that prints a square with the character #.

    Returns :
        Nothing

    Raises :
        TypeError in case the size is not int
        TypeError in case the size is higher or equal to zero.
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("{}".format("#"), end="")
        print()
