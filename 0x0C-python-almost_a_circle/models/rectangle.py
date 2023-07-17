#!/usr/bin/python3
"""
0x0C. Python - Almost a circle
"""

from models.base import Base


class Rectangle(Base):
    """
    class Rectangle that inherits from Base:
        Task 2:
            Private instance attributes, each with its
            own public getter and setter:
                __width -> width
                __height -> height
                __x -> x
                __y -> y
            Class constructor: def __init__(self, width,
            height, x=0, y=0, id=None):
            Call the super class with id - this super call
            with use the logic of the __init__ of the Base class
            Assign each argument width, height, x and y to the
            right attribute
        Task 3:
            validation of all setter methods and instantiation (id excluded):
                If the input is not an integer, raise the TypeError exception
                If width or height <= 0, raise a ValueError exception
                If x or y < 0, raise the ValueError exception
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
