"""
0x0C. Python - Almost a circle
"""
from models.base import Base
from models.rectangle import Rectangle
import unittest
import os
from io import StringIO
import sys
from contextlib import redirect_stdout


class TestRectangle(unittest.TestCase):
    """
        All your files, classes and methods must be unit tested
        and be PEP 8 validated.
        command : python3 -m unittest discover tests
    """

    def test_area(self):
        """Testing the method area"""
        obj = Rectangle(3, 2)
        self.assertIsInstance(obj, Rectangle)
        obj_area = obj.area()
        self.assertEqual(6, obj_area)
        obj = Rectangle(6, 2)
        obj_area = obj.area()
        self.assertEqual(12, obj_area)

    def test_display(self):
        """Testing the method display"""
        obj = Rectangle(4, 3, 2, 1)
        output_buffer = StringIO()
        expected_output = "####\n  ####\n  ####"
        with redirect_stdout(output_buffer):
            obj.display()
        printed_output = output_buffer.getvalue().strip()
        self.assertEqual(printed_output, expected_output)

    def test___str__(self):
        """Testing the method __str__"""
        obj = Rectangle(4, 6, 2, 1, 12)
        output = obj.__str__()
        expected_output = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(output, expected_output)
        obj_2 = Rectangle(5, 5, 1)
        output = obj_2.__str__()
        expected_output = "[Rectangle] (4) 1/0 - 5/5"
        self.assertEqual(output, expected_output)

    def test_update(self):
        """Testing the method update"""
        obj = Rectangle(3, 10, 10, 10, 10)
        obj.update(13, 8, 7, 9, 12)
        self.assertEqual(obj.id, 13)
        self.assertEqual(obj.width, 8)
        self.assertEqual(obj.height, 7)
        self.assertEqual(obj.x, 9)
        self.assertEqual(obj.y, 12)
