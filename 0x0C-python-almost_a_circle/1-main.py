#!/usr/bin/python3
""" 1-main """
from models.base import Base
import inspect

if __name__ == "__main__":

    """
        0)
        Main from Task.
        Expected output :   |        Got:
        -------------------------------------------
                1           |         1
                2           |         2
                3           |         3
                12          |         12
                4           |         4
    """
    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)

    """
        1)
        Main from QA.
        Expected output = OK
        Got = OK
    """
    base_import = __import__('models.base').base

    if base_import is None:
        print("Can't import models.base")
        exit(1)

    base_class = base_import.__dict__.get('Base')
    if base_class is None:
        print("Can't find class Base in models.base")
        exit(1)

    if not inspect.isclass(base_class):
        print("Base is not a class")
        exit(1)

    print("OK", end="")

    """
        2)
        Main from QA.
        Expected output = OK
        Got = OK
    """
    b = Base()
    if b is None:
        print("Can't create Base")
        exit(1)

    print("OK", end="")

    """
        3)
        Main from QA.
        Expected output = OK
        Got = OK
    """
    b = Base(12)
    if b is None:
        print("Can't create Base")
        exit(1)

    if b.id != 12:
        print("ID is not the same as the one pass as argument: {}".format(b.id))
        exit(1)

    print("OK", end="")

    """
        3)
        Main from QA.
        Expected output = OK
        Got = OK
    """
    b = Base()
    if b is None:
        print("Can't create Base")
        exit(1)

    if b.id != 1:
        print("ID is not equal to 1: {}".format(b.id))
        exit(1)

    print("OK", end="")

    """
        4)
        Main from QA.
        Expected output = OK
        Got = OK
    """
    b = Base()
    if b is None:
        print("Can't create Base")
        exit(1)

    if b.id != 1:
        print("ID is not equal to 1: {}".format(b.id))
        exit(1)

    for i in range(2):
        btmp = Base()

    btest = Base()
    if btest is None:
        print("Can't create Base")
        exit(1)

    if btest.id != 4:
        print("ID is not equal to 4 after 3 other creations: {}".format(btest.id))
        exit(1)

    print("OK", end="")
