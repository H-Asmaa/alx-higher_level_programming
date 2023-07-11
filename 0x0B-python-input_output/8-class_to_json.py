#!/usr/bin/python3
"""
0x0B. Python - Input/Output
"""


def class_to_json(obj):
    """A  function that returns the dictionary description
    with simple data structure (list, dictionary, string,
    integer and boolean) for JSON serialization of an object
    As a solution we can elso use return obj.__dict__
    """
    return vars(obj)
