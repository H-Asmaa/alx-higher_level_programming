#!/usr/bin/python3
""" 19-main """
from models.rectangle import Rectangle
from models.square import Square
import os
import json

if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    list_rectangles_input = [r1, r2]

    Rectangle.save_to_file(list_rectangles_input)

    list_rectangles_output = Rectangle.load_from_file()

    for rect in list_rectangles_input:
        print("[{}] {}".format(id(rect), rect))

    print("---")

    for rect in list_rectangles_output:
        print("[{}] {}".format(id(rect), rect))

    print("---")
    print("---")

    s1 = Square(5)
    s2 = Square(7, 9, 1)
    list_squares_input = [s1, s2]

    Square.save_to_file(list_squares_input)

    list_squares_output = Square.load_from_file()

    for square in list_squares_input:
        print("[{}] {}".format(id(square), square))

    print("---")

    for square in list_squares_output:
        print("[{}] {}".format(id(square), square))

    """
        Main from QA.
        Expected output = OK
        Got = OK
    """
    file_path = "Rectangle.json"
    if os.path.exists(file_path):
        os.remove(file_path)

    res = Rectangle.load_from_file()

    if res is None:
        print("load_from_file doesn't return an empty"
              " list when the file doesn't exist")
        exit(1)

    if len(res) != 0:
        print("load_from_file doesn't return an empty"
              " list when the file doesn't exist")
        exit(1)

    print("OK", end="")
