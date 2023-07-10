#!/usr/bin/python3
"""
0x0A. Python - Inheritance
"""


class MyList(list):
    """The class MyList that inherits from list:
        Public instance method:
        - def print_sorted(self):
                # that prints the list, sorted (ascending sort)s
                # asssuming that elements are of type int
    """

    def print_sorted(self):
        """Public instance method"""
        sorted_list = sorted(self, key=None, reverse=False)
        print(sorted_list)
