#!/usr/bin/python3
"""
0x0A. Python - Inheritance
"""


def inherits_from(obj, a_class):
    """function that returns True if the object is an
    instance of a class that inherited (directly/indirectly)
    from the specified class ; otherwise False."""
    if isinstance(obj, a_class) and not type(obj) is a_class:
        return True
    return False
