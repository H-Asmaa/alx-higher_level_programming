#!/usr/bin/python3
"""0x08. Python - More Classes and Objects"""


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
    __width = None
    __height = None

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int):
            self.__width = value
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @height.setter
    def height(self, value):
        if isinstance(value, int):
            self.__height = value
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
