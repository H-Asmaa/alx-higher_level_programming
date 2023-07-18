#!/usr/bin/python3
""" 2-main """
from models.rectangle import Rectangle
import inspect

if __name__ == "__main__":

    """
        0)
        Main from Task.
        Expected output :   |        Got:
        -------------------------------------------
                1           |         1
                2           |         2
                12          |         12
    """
    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)

    """
        1)
        Main from QA.
        Expected output = OK
        Got = OK
    """
    rectangle_import = __import__('models.rectangle').rectangle

    if rectangle_import is None:
        print("Can't import models.rectangle")
        exit(1)

    rectangle_class = rectangle_import.__dict__.get('Rectangle')
    if rectangle_class is None:
        print("Can't find class Rectangle in models.rectangle")
        exit(1)

    if not inspect.isclass(rectangle_class):
        print("Rectangle is not a class")
        exit(1)

    """
        2)
        Main from QA.
        Expected output = OK
        Got = OK
    """
    r = Rectangle(12, 14)
    if r is None:
        print("Can't create Rectangle")
        exit(1)

    if r._Rectangle__width != 12:
        print("Wrong width: {}".format(r._Rectangle__width))
        exit(1)

    if r._Rectangle__height != 14:
        print("Wrong height: {}".format(r._Rectangle__height))
        exit(1)

    if r._Rectangle__x != 0:
        print("Wrong x: {}".format(r._Rectangle__x))
        exit(1)

    if r._Rectangle__y != 0:
        print("Wrong y: {}".format(r._Rectangle__y))
        exit(1)

    if r.id != 1:
        print("ID is not initialized at 1")
        exit(1)

    print("OK", end="")

    """
        3)
        Main from QA.
        Expected output = OK
        Got = OK
    """
    r = Rectangle(12, 14, 4)
    if r is None:
        print("Can't create Rectangle")
        exit(1)

    if r._Rectangle__width != 12:
        print("Wrong width: {}".format(r._Rectangle__width))
        exit(1)

    if r._Rectangle__height != 14:
        print("Wrong height: {}".format(r._Rectangle__height))
        exit(1)

    if r._Rectangle__x != 4:
        print("Wrong x: {}".format(r._Rectangle__x))
        exit(1)

    if r._Rectangle__y != 0:
        print("Wrong y: {}".format(r._Rectangle__y))
        exit(1)

    if r.id != 1:
        print("ID is not initialized at 1")
        exit(1)

    print("OK", end="")

    """
        4)
        Main from QA.
        Expected output = OK
        Got = OK
    """
    r = Rectangle(12, 14, 4, 5, 10)
    if r is None:
        print("Can't create Rectangle")
        exit(1)

    if r._Rectangle__width != 12:
        print("Wrong width: {}".format(r._Rectangle__width))
        exit(1)

    if r._Rectangle__height != 14:
        print("Wrong height: {}".format(r._Rectangle__height))
        exit(1)

    if r._Rectangle__x != 4:
        print("Wrong x: {}".format(r._Rectangle__x))
        exit(1)

    if r._Rectangle__y != 5:
        print("Wrong y: {}".format(r._Rectangle__y))
        exit(1)

    if r.id != 10:
        print("ID is not initialized at 10")
        exit(1)

    print("OK", end="")

    """
        5)
        Main from QA.
        Expected output = OK
        Got = OK
    """
    r = Rectangle(12, 14, 4, 5, 10)
    if r is None:
        print("Can't create Rectangle")
        exit(1)

    if r._Rectangle__width != 12:
        print("Wrong private width: {}".format(r._Rectangle__width))
        exit(1)

    if r.width != 12:
        print("Wrong width getter: {}".format(r._Rectangle__width))
        exit(1)

    r.width = 5

    if r._Rectangle__width != 5:
        print("Wrong private width: {}".format(r._Rectangle__width))
        exit(1)

    if r.width != 5:
        print("Wrong width getter: {}".format(r._Rectangle__width))
        exit(1)

    print("OK", end="")

    """
        6)
        Main from QA.
        Expected output = OK
        Got = OK
    """
    r = Rectangle(12, 14, 4, 5, 10)
    if r is None:
        print("Can't create Rectangle")
        exit(1)

    if r._Rectangle__x != 4:
        print("Wrong private x: {}".format(r._Rectangle__x))
        exit(1)

    if r.x != 4:
        print("Wrong x getter: {}".format(r._Rectangle__x))
        exit(1)

    r.x = 5

    if r._Rectangle__x != 5:
        print("Wrong private x: {}".format(r._Rectangle__x))
        exit(1)

    if r.x != 5:
        print("Wrong x getter: {}".format(r._Rectangle__x))
        exit(1)

    print("OK", end="")

    """
        7)
        Main from QA.
        Expected output = OK
        Got = OK
    """
    r = Rectangle(12, 14, 4, 5, 10)
    if r is None:
        print("Can't create Rectangle")
        exit(1)

    if r._Rectangle__y != 5:
        print("Wrong private y: {}".format(r._Rectangle__y))
        exit(1)

    if r.y != 5:
        print("Wrong y getter: {}".format(r._Rectangle__y))
        exit(1)

    r.y = 13

    if r._Rectangle__y != 13:
        print("Wrong private y: {}".format(r._Rectangle__y))
        exit(1)

    if r.y != 13:
        print("Wrong y getter: {}".format(r._Rectangle__y))
        exit(1)

    print("OK", end="")
