#!/usr/bin/python3
"""
0x0C. Python - Almost a circle
"""

import json


class Base:
    """
    Class Base:
        Task 1:
            A folder named models with an empty file __init__.py inside
            with this file, the folder will become a Python package
            private class attribute __nb_objects = 0
            class constructor: def __init__(self, id=None)::
                - if id is not None, assign the public instance attribute
                id with this argument value - you can assume id is an integer
                and you don’t need to test the type of it
                - else, increment __nb_objects and assign the new value to
                the public instance attribute id
        Task 15:
            Adding the static method def to_json_string(list_dictionaries):
            that returns the JSON string representation of list_dictionaries:
                - list_dictionaries is a list of dictionaries
                - If list_dictionaries is None or empty, return "[]"
                - Otherwise, return the JSON string representations
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)