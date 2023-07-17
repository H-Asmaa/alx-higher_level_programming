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
            Validation of all setter methods and instantiation (id excluded):
                If the input is not an integer, raise the TypeError exception
                If width or height <= 0, raise a ValueError exception
                If x or y < 0, raise the ValueError exception
        Task 4:
            Adding the public method def area(self): that returns the area
            value of the Rectangle instance.
        Task 5:
            Adding the public method def display(self): that prints in stdout
            the Rectangle instance with the character #
            no need to handle x and y.
        Task 6:
            Overriding the __str__ method from the object class so that it
            returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
        Task 7:
            Improving the public method def display(self): to print the
            Rectangle instance with the character # by taking care of x and y
            With x and y defining the position of the rectangle.
                x - the horizontal displacement
                y - the vertical displacement
        Task 8:
            Adding the public method def update(self, *args): that assigns
            an argument to each attribute:
                - 1st argument should be the id attribute
                - 2nd argument should be the width attribute
                - 3rd argument should be the height attribute
                - 4th argument should be the x attribute
                - 5th argument should be the y attribute
            This type of argument is called a “no-keyword argument” - Argument
            order is super important.
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

    def area(self):
        return self.__width * self.__height

    def display(self):
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for o in range(self.__x):
                print(end=" ")
            for j in range(self.__width):
                print("{}".format("#"), end="")
            print()

    def __str__(self):
        width = self.__width
        height = self.__height
        return f"({self.id}) {self.__x}/{self.__y} - {width}/{height}"

    def update(self, *args):
        attribute_names = ['id', 'width', 'height', 'x', 'y']
        for i in range(min(len(attribute_names), len(args))):
            setattr(self, attribute_names[i], args[i])
