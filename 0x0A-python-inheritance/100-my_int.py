#!/usr/bin/python3
"""
0x0A. Python - Inheritance
"""


class MyInt(int):
    """class MyInt :
    - MyInt is a rebel. MyInt has == and != operators inverted
    """

    def __eq__(self, __value: object) -> bool:
        return super().__ne__(__value)

    def __ne__(self, __value: object) -> bool:
        return super().__eq__(__value)
