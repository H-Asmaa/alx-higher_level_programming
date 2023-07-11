#!/usr/bin/python3
"""
0x0B. Python - Input/Output
"""
import json


def to_json_string(my_obj):
    """A function that returns the JSON representation of an object (string)
    json.dumps : turns an object into a json string, raises a traceback in
    case the object is not a json serializable.
    """
    return json.dumps(my_obj)
