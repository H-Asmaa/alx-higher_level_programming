#!/usr/bin/python3
"""
0x0B. Python - Input/Output
"""


def read_file(filename=""):
    """A function that reads a text file (UTF8) and prints it to stdout."""
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            print(line, end="")
