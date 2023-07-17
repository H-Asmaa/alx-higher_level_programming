#!/usr/bin/python3
"""
0x0C. Python - Almost a circle
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square that inherits from Rectangle:
        Task 10:
            Class constructor:
            def __init__(self, size, x=0, y=0, id=None):
                - Call the super class with id, x, y, width and
                height, this super call will use the logic of the
                __init__ of the
                Rectangle class. The width and height must be
                assigned to the value of size.
                - You must not create new attributes for this class,
                use all attributes of Rectangle - As reminder: a Square
                is a Rectangle with the same width and height
                - All width, height, x and y validation must inherit from
                Rectangle - same behavior in case of wrong data
            The overloading __str__ method should return [Square] (<id>)
            <x>/<y> - <size> - in our case, width or height
            A Square is a special Rectangle, so it makes sense this class
            Square inherits from Rectangle. Now you have a Square class
            who has the same attributes and same methods.
        Task 11:
            Adding the public getter and setter size
                - The setter should assign (in this order) the width and
                the height - with the same value
                - The setter should have the same value validation as the
                Rectangle for width and height - No need to change the
                exception error message (It should be the one from width)
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id=None)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
