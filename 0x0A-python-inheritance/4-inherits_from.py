#!/usr/bin/python3
"""
0x0A. Python - Inheritance
"""


def inherits_from(obj, a_class):
    """function that returns True if the object is an
    instance of a class that inherited (directly/indirectly)
    from the specified class ; otherwise False."""
    cls = type(obj).__base__
    while cls != object:
        if issubclass(cls, a_class):
            return True
        cls = cls.__base__
    return False
