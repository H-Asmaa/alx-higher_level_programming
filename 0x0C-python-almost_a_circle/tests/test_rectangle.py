"""
0x0C. Python - Almost a circle
"""
from models.base import Base
from models.rectangle import Rectangle
import unittest
import os


class TestRectangle(unittest.TestCase):
    """
        All your files, classes and methods must be unit tested
        and be PEP 8 validated.
        command : python3 -m unittest discover tests
    """

    def test_area(self):
        """Testing the method area"""
        obj = Rectangle(3, 2)
        obj_area = obj.area()
        self.assertEqual(6, obj_area)
        obj = Rectangle(6, 2)
        obj_area = obj.area()
        self.assertEqual(12, obj_area)
