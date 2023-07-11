#!/usr/bin/python3
"""
0x0B. Python - Input/Output
"""


def read_file(filename=""):
    """A function that reads a text file (UTF8) and prints it to stdout."""
    with open('my_file_0.txt', 'r', encoding="UTF-8") as f:
        read = f.read()
    print(read)
