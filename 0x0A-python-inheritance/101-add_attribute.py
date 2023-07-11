#!/usr/bin/python3
"""
0x0A. Python - Inheritance
"""


def add_attribute(obj, attr, attr_val):
    """A function that adds a new attribute to an object if
    it’s possible:"""
    if hasattr(obj, "__dict__"):
        setattr(obj, attr, attr_val)
    else:
        raise TypeError("can't add new attribute")
