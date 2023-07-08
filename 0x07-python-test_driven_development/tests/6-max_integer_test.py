#!/usr/bin/python3
import unittest
"""Module to find the max integer in a list
"""

max_integer = __import__('6-max_integer').max_integer

class Test_method(unittest.TestCase):
    """unittest class"""
    def test_max_end(self):
        test = max_integer([1, 4, 8, 10])
        self.assertEqual(test, 10)

    def test_max_begin(self):
        test = max_integer([333, 4, -8, 100])
        self.assertEqual(test, 333)

    def test_max_middle(self):
        test = max_integer([333, 4, 800, 100])
        self.assertEqual(test, 800)

    def test_max_negative(self):
        test = max_integer([-333, -4, -800, -100])
        self.assertEqual(test, -4)

    def test_ampty(self):
        test = max_integer([])
        self.assertEqual(test, None)

    def test_one_elm(self):
        test = max_integer([1])
        self.assertEqual(test, 1)


if __name__ == "__main__":
    unittest.main()
