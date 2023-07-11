#!/usr/bin/python3
"""
0x0B. Python - Input/Output
"""


def write_file(filename="", text=""):
    """A function that writes a string to a text file
    (UTF8) and returns the number of characters written"""
    with open(filename, "w", encoding="UTF-8") as f:
        char_count = 0
        for i in text:
            f.write(i)
            char_count += 1
    return char_count
