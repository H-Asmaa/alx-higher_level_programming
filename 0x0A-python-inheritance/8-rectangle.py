#!/usr/bin/python3
"""
0x0A. Python - Inheritance
"""


class BaseGeometry():
    """class BaseGeometry:
            Public instance method: def area(self):
                # that raises an Exception with the message
                area() is not implemented
            Public instance method:
                # def integer_validator(self, name, value):
                that validates value:
                # you can assume name is always a string
                # if value is not an integer: raise a TypeError exception
                with the message <name> must be an integer
                # if value is less or equal to 0: raise a ValueError
                exception with the message <name> must be greater than 0
        """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Class Rectangle
    Instantiation with width and height:
    def __init__(self, width, height):
        - width and height must be private.
        No getter or setter
        - width and height must be positive integers,
        validated by integer_validator
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height
        super().integer_validator("width", self.width)
        super().integer_validator("height", self.height)
