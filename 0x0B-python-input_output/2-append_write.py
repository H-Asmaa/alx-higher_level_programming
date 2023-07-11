#!/usr/bin/python3
"""
0x0B. Python - Input/Output
"""


def append_write(filename="", text=""):
    """A function that appends text to a text file
    and returns the number of characters added"""
    with open(filename, "a", encoding="UTF-8") as f:
        char_count = 0
        for i in text:
            f.write(i)
            char_count += 1
    return char_count
