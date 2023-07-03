#!/usr/bin/python3

"""
0x08. Python - More Classes and Objects
"""


class Rectangle:
    """The class Rectangle
    Private instance attribute: width:
        - property def width(self): to retrieve it
        - property setter def width(self, value): to set it:
                        # width must be an integer, otherwise raise a TypeError
                        exception with the message width must be an integer
                        # if width is less than 0, raise a ValueError exception
                with the message width must be >= 0

        Private instance attribute: height:
                same thing goes exactly as width.
        Instantiation with optional width and height:
        def __init__(self, width=0, height=0):
    """
    def __init__(self, width=0, height=0):
        """__init__ dunder
        Arguments:
            width : the width of rectangle
            height : the height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter
                Args:
            value: The new width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter
                Args:
            value: The new height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
