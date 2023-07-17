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
        Task 16:
            Adding the class method def save_to_file(cls, list_objs): that
            writes the JSON string representation of list_objs to a file:
                - list_objs is a list of instances who inherits of Base
                - If list_objs is None, save an empty list
                - The filename must be: <Class name>.json ex: Rectangle.json
                - You must use the static method to_json_string
                - You must overwrite the file if it already exists
        Task 17:
            Adding the static method def from_json_string(json_string): that
            returns the list of the JSON string representation json_string:
                - json_string is a string representing a list of dictionaries
                - If json_string is None or empty, return an empty list
                - Otherwise, return the list represented by json_string

            PS: We can unpack the dictionary using ** notation to pass the
            attribute-value pairs as keyword arguments.
        Task 18:
            Adding the class method def create(cls, **dictionary): that
            returns an instance with all attributes already set:
                - **dictionary is like a double pointer to a dictionary
                - To use the update method to assign all attributes, you must
                create a “dummy” instance before:
                - Create a Rectangle or Square instance with “dummy” mandatory
                attributes (width, height, size, etc.)
                - Call update instance method to this “dummy” instance to apply
                your real values
                - You must use the method def update(self, *args, **kwargs)
                - **dictionary must be used as **kwargs of the method update
                - You are not allowed to use eval
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        file_name = cls.__name__ + ".json"
        list_ = []
        with open(file_name, "w", encoding="UTF-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                for i in list_objs:
                    list_.append(i.to_dictionary())
                f.write(Base.to_json_string(list_))

    def from_json_string(json_string):
        if json_string is None:
            return ("[]")
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        instance_dict = {}
        for key, val in dictionary.items():
            instance_dict[key] = val
        instance = cls(**instance_dict)
        instance.update(**instance_dict)
        return instance
