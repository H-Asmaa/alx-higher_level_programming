#!/usr/bin/python3
""" 8-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 10, 10, 10)
    print(r1)
    """
    In this specific test case, r1 = Rectangle(10, 10, 10, 10)
    the id attribute is assigned the value of 1 because it is
    the first instance of the Rectangle class created in your
    code. The __nb_objects counter is incremented when this
    instance is created, and the incremented value is assigned
    to the id attribute.
    """
    r1.update(89)
    print(r1)

    r1.update(89, 2)
    print(r1)

    r1.update(89, 2, 3)
    print(r1)

    r1.update(89, 2, 3, 4)
    print(r1)

    r1.update(89, 2, 3, 4, 5)
    print(r1)
