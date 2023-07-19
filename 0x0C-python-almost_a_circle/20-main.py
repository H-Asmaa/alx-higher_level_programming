#!/usr/bin/python3
""" 100-main """
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import random
import os


if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    list_rectangles_input = [r1, r2]

    Rectangle.save_to_file_csv(list_rectangles_input)

    list_rectangles_output = Rectangle.load_from_file_csv()

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

    Square.save_to_file_csv(list_squares_input)

    list_squares_output = Square.load_from_file_csv()

    for square in list_squares_input:
        print("[{}] {}".format(id(square), square))

    print("---")

    for square in list_squares_output:
        print("[{}] {}".format(id(square), square))

    """
        1)
        Main from QA.
        Expected output = OK
        Got = OK
    """
    save_to_file_csv_fct = Base.__dict__.get("save_to_file_csv")
    if save_to_file_csv_fct is None:
        print("Base doesn't have method save_to_file_csv")
        exit(1)
    print("OK", end="")

    """
        2)
        Main from QA.
        Expected output = OK
        Got = OK
    """
    load_from_file_csv_fct = Base.__dict__.get("load_from_file_csv")
    if load_from_file_csv_fct is None:
        print("Base doesn't have method load_from_file_csv")
        exit(1)
    print("OK", end="")

    """
        3)
        Main from QA.
        Expected output = OK
        Got = OK
    """
file_path = "Rectangle.csv"
if os.path.exists(file_path):
    os.remove(file_path)

list_objs = []
for i in range(0, 5):
    list_objs.append(Rectangle(random.randrange(1, 100, 2), random.randrange(
        1, 100, 2), random.randrange(1, 100, 2), random.randrange(1, 100, 2)))

Rectangle.save_to_file_csv(list_objs)

if not os.path.exists(file_path):
    print("save_to_file_csv doesn't save to disk the list of Rectangle")
    exit(1)

list_objs_res = Rectangle.load_from_file_csv()

if list_objs_res is None:
    print("load_from_file_csv doesn't return a list")
    exit(1)

if len(list_objs_res) != len(list_objs):
    print("load_from_file_csv doesn't return a list")
    exit(1)

for i in range(0, len(list_objs)):
    obj = list_objs[i]
    if i >= len(list_objs_res):
        print("load_from_file_csv doesn't return all objects")
        exit(1)

    obj_res = list_objs_res[i]

    if obj_res.id != obj.id:
        print("Rectangle {} not found".format(obj))
        exit(1)

    if obj_res.width != obj.width:
        print("Rectangle {} doesn't match with the original: {}".format(obj_res, obj))
        exit(1)

    if obj_res.height != obj.height:
        print("Rectangle {} doesn't match with the original: {}".format(obj_res, obj))
        exit(1)

    if obj_res.x != obj.x:
        print("Rectangle {} doesn't match with the original: {}".format(obj_res, obj))
        exit(1)

    if obj_res.y != obj.y:
        print("Rectangle {} doesn't match with the original: {}".format(obj_res, obj))
        exit(1)

print("OK", end="")

"""
        4)
        Main from QA.
        Expected output = OK
        Got = OK
    """
file_path = "Square.csv"
if os.path.exists(file_path):
    os.remove(file_path)

list_objs = []
for i in range(0, 5):
    list_objs.append(Square(random.randrange(1, 100, 2), random.randrange(1, 100, 2), random.randrange(1, 100, 2)))

Square.save_to_file_csv(list_objs)

if not os.path.exists(file_path):
    print("save_to_file_csv doesn't save to disk the list of Square")
    exit(1)

list_objs_res = Square.load_from_file_csv()

if list_objs_res is None:
    print("load_from_file_csv doesn't return a list")
    exit(1)

if len(list_objs_res) != len(list_objs):
    print("load_from_file_csv doesn't return a list")
    exit(1)

for i in range(0, len(list_objs)):
    obj = list_objs[i]
    if i >= len(list_objs_res):
        print("load_from_file_csv doesn't return all objects")
        exit(1)

    obj_res = list_objs_res[i]

    if obj_res.id != obj.id:
        print("Square {} not found".format(obj))
        exit(1)

    if obj_res.size != obj.size:
        print("Square {} doesn't match with the original: {}".format(obj_res, obj))
        exit(1)

    if obj_res.x != obj.x:
        print("Square {} doesn't match with the original: {}".format(obj_res, obj))
        exit(1)

    if obj_res.y != obj.y:
        print("Square {} doesn't match with the original: {}".format(obj_res, obj))
        exit(1)

print("OK", end="")
