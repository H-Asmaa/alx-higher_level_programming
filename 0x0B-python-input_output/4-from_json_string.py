#!/usr/bin/python3
"""
0x0B. Python - Input/Output
"""
import json


def from_json_string(my_str):
    """A function that returns an object (Python data structure)
    represented by a JSON string
    json.loads() : a method that trasforms a json string into
    it's original type"""
    return json.loads(my_str)
