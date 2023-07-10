#!/usr/bin/python3
"""
0x0A. Python - Inheritance
"""


def is_kind_of_class(obj, a_class):
    """A function that returns True if the object is an
    instance of, or if the object is an instance of a
    class that inherited from, the specified class"""
    if isinstance(obj, a_class):
        return True
    return False
