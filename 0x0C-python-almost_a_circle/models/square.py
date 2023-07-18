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
        Task 12:
            Adding the public method def update(self, *args, **kwargs)
            that assigns attributes:
                *args is the list of arguments - no-keyworded arguments
                    - 1st argument should be the id attribute
                    - 2nd argument should be the size attribute
                    - 3rd argument should be the x attribute
                    - 4th argument should be the y attribute
                **kwargs can be thought of as a double pointer to a
                dictionary: key/value (keyworded arguments)
                **kwargs must be skipped if *args exists and is not empty
                Each key in this dictionary represents an attribute to
                the instance
        Task 14:
            Adding the public method def to_dictionary(self): that returns
            the dictionary representation of a Square:
            This dictionary must contain:
                - id
                - size
                - x
                - y
    """

    def __init__(self, size, x=0, y=0, id=None):
        """__init__ method"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """size getter method"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter method"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update method"""
        attribute_names = ['id', 'size', 'x', 'y']
        if args:
            for i in range(min(len(attribute_names), len(args))):
                setattr(self, attribute_names[i], args[i])
        else:
            for key, val in kwargs.items():
                if key in attribute_names:
                    setattr(self, key, val)

    def to_dictionary(self):
        """to_dictionary method"""
        dictionnary = {'id': self.id,
                       'size': self.size,
                       'x': self.x,
                       'y': self.y}
        return dictionnary
