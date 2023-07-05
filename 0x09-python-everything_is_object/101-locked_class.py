#!/usr/bin/python3
"""Class LockedClass"""


class LockedClass:
    """A class that prevents the user from dynamically creating new instance
    attributes, except if the new instance attribute is called first_name.
    __slots__ : attribute altering"""
    __slots__ = ['first_name']
