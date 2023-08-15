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
from unittest.mock import patch


class TestRectangle(unittest.TestCase):
    """
        All your files, classes and methods must be unit tested
        and be PEP 8 validated.
        command : python3 -m unittest discover tests
    """

    def test_attributes_validation(self):
        """Testing tracebacks for attributes"""
        """----WIDTH----"""
        with self.assertRaises(TypeError) as traceback:
            instance = Rectangle("h", 2)
        self.assertEqual(str(traceback.exception), "width must be an integer")
        with self.assertRaises(ValueError) as traceback:
            instance = Rectangle(-1, 2)
        self.assertEqual(str(traceback.exception), "width must be > 0")
        with self.assertRaises(ValueError) as traceback:
            instance = Rectangle(0, 2)
        self.assertEqual(str(traceback.exception), "width must be > 0")
        """----HEIGHT----"""
        with self.assertRaises(TypeError) as traceback:
            instance = Rectangle(1, "h")
        self.assertEqual(str(traceback.exception), "height must be an integer")
        with self.assertRaises(ValueError) as traceback:
            instance = Rectangle(1, -2)
        self.assertEqual(str(traceback.exception), "height must be > 0")
        with self.assertRaises(ValueError) as traceback:
            instance = Rectangle(1, 0)
        self.assertEqual(str(traceback.exception), "height must be > 0")
        """----X----"""
        with self.assertRaises(TypeError) as traceback:
            instance = Rectangle(1, 2, "d", 1)
        self.assertEqual(str(traceback.exception), "x must be an integer")
        with self.assertRaises(ValueError) as traceback:
            instance = Rectangle(1, 2, -1)
        self.assertEqual(str(traceback.exception), "x must be >= 0")
        """----Y----"""
        with self.assertRaises(TypeError) as traceback:
            instance = Rectangle(1, 2, 1, "d")
        self.assertEqual(str(traceback.exception), "y must be an integer")
        with self.assertRaises(ValueError) as traceback:
            instance = Rectangle(1, 2, 1, -7)
        self.assertEqual(str(traceback.exception), "y must be >= 0")

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

    def test_update_with_args(self):
        """Testing the method update with args"""
        obj = Rectangle(3, 10, 10, 10, 10)
        obj.update(13, 8, 7, 9, 12)
        self.assertEqual(obj.id, 13)
        self.assertEqual(obj.width, 8)
        self.assertEqual(obj.height, 7)
        self.assertEqual(obj.x, 9)
        self.assertEqual(obj.y, 12)
        obj.update(6, 5, 4)
        self.assertEqual(obj.id, 6)
        self.assertEqual(obj.width, 5)
        self.assertEqual(obj.height, 4)

    def test_update_with_kwargs(self):
        """Testing the method update with kwargs"""
        obj = Rectangle(3, 10, 10, 10, 10)
        obj.update(id=11, width=8, height=5, x=9, y=12)
        self.assertEqual(obj.id, 11)
        self.assertEqual(obj.width, 8)
        self.assertEqual(obj.height, 5)
        self.assertEqual(obj.x, 9)
        self.assertEqual(obj.y, 12)
        obj.update(height=30, x=10, y=2)
        self.assertEqual(obj.id, 11)
        self.assertEqual(obj.width, 8)
        self.assertEqual(obj.height, 30)
        self.assertEqual(obj.x, 10)
        self.assertEqual(obj.y, 2)

    def test_update_with_dictionnary(self):
        """Testing the method update with dictionary"""
        obj = Rectangle(3, 10, 10, 10, 10)
        obj.update(**{'id': 89})
        self.assertEqual(obj.id, 89)
        obj.update(**{'id': 89, 'width': 1})
        self.assertEqual(obj.id, 89)
        self.assertEqual(obj.width, 1)
        obj.update(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(obj.id, 89)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 2)
        obj.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(obj.id, 89)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 2)
        self.assertEqual(obj.x, 3)
        obj.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(obj.id, 89)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 2)
        self.assertEqual(obj.x, 3)
        self.assertEqual(obj.y, 4)

    def test_update_with_kwargs_and_args(self):
        """Testing the method update with kwargs and args"""
        obj = Rectangle(10, 20, 5, 5, 1)
        obj.update()
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.width, 10)
        self.assertEqual(obj.height, 20)
        self.assertEqual(obj.x, 5)
        self.assertEqual(obj.y, 5)

    def test_to_dictionary(self):
        """Testing the method to_dictionary"""
        obj = Rectangle(10, 2, 1, 9)
        output = obj.to_dictionary()
        self.assertIsInstance(output, dict)
