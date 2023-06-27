#!/usr/bin/python3
"""Completing the class Square"""


class Square:
    """Class Square with Private instance attribute: size
    The method __init__ contains exceptions for when size
    is not an int and when it's less than zero.

    The initialisation of size to zero will serve it's pu
    -rpose when the size is not given.

    The implementation of the method area, that returns t
    -he square of a given size."""
    __size = None

    def __init__(self, size=0):
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        return self.__size ** 2
