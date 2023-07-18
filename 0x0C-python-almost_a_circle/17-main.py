#!/usr/bin/python3
""" 17-main """
from models.rectangle import Rectangle
from models.base import Base
import json

if __name__ == "__main__":

    list_input = [
        {'id': 89, 'width': 10, 'height': 4},
        {'id': 7, 'width': 1, 'height': 7}
    ]
    json_list_input = Rectangle.to_json_string(list_input)
    list_output = Rectangle.from_json_string(json_list_input)
    print("[{}] {}".format(type(list_input), list_input))
    print("[{}] {}".format(type(json_list_input), json_list_input))
    print("[{}] {}".format(type(list_output), list_output))

    """
        Main from QA.
        Expected output = OK
        Got = OK
    """
    res = Base.from_json_string(None)

    if res is None:
        print("from_json_string doesn't return a"
              " list of dictionaries: {}".format(res))
        exit(1)

    if type(res) is not list:
        print("from_json_string doesn't return a"
              " list of dictionaries: {}".format(res))
        exit(1)

    if len(res) != 0:
        print("from_json_string doesn't return a"
              " list of dictionaries: {}".format(res))
        exit(1)

    print("OK", end="")
