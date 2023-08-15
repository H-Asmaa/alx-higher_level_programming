"""
0x0C. Python - Almost a circle
"""
from models.base import Base
from models.square import Square
import unittest
from unittest.mock import patch


class TestSquare(unittest.TestCase):
    """
        All your files, classes and methods must be unit tested
        and be PEP 8 validated.
        command : python3 -m unittest discover tests
    """

    def test_attributes(self):
        """Testing attributes"""
        obj = Square(1)
        self.assertEqual(obj.size, 1)
        obj = Square(1, 2)
        self.assertEqual(obj.size, 1)
        self.assertEqual(obj.x, 2)
        obj = Square(1, 2, 3)
        self.assertEqual(obj.size, 1)
        self.assertEqual(obj.x, 2)
        self.assertEqual(obj.y, 3)
        obj = Square(1, 2, 3, 4)
        self.assertEqual(obj.id, 4)
        self.assertEqual(obj.size, 1)
        self.assertEqual(obj.x, 2)
        self.assertEqual(obj.y, 3)

    def test_attributes_validation(self):
        """Testing attributes validation"""
        """---WIDTH---"""
        with self.assertRaises(TypeError) as traceback:
            isinstance = Square("a")
        self.assertEqual(str(traceback.exception), "width must be an integer")
        with self.assertRaises(ValueError) as traceback:
            isinstance = Square(-1)
        self.assertEqual(str(traceback.exception), "width must be > 0")
        """---X---"""
        with self.assertRaises(TypeError) as traceback:
            isinstance = Square(1, "a")
        self.assertEqual(str(traceback.exception), "x must be an integer")
        with self.assertRaises(ValueError) as traceback:
            isinstance = Square(1, -1)
        self.assertEqual(str(traceback.exception), "x must be >= 0")
        """---Y---"""
        with self.assertRaises(TypeError) as traceback:
            isinstance = Square(1, 2, "a")
        self.assertEqual(str(traceback.exception), "y must be an integer")
        with self.assertRaises(ValueError) as traceback:
            isinstance = Square(1, 2, -1)
        self.assertEqual(str(traceback.exception), "y must be >= 0")

    def test___str__(self):
        """Testing the method __str__"""
        obj = Square(4, 6, 1, 12)
        output = obj.__str__()
        expected_output = "[Square] (12) 6/1 - 4"
        self.assertEqual(output, expected_output)
        obj_2 = Square(5, 5, 1)
        output = obj_2.__str__()
        expected_output = "[Square] (9) 5/1 - 5"
        self.assertEqual(output, expected_output)

    def test_update_with_args(self):
        """Testing the method update with args"""
        obj = Square(3, 10, 10, 10)
        obj.update(13, 7, 9, 12)
        self.assertEqual(obj.id, 13)
        self.assertEqual(obj.size, 7)
        self.assertEqual(obj.x, 9)
        self.assertEqual(obj.y, 12)
        obj.update(6, 5)
        self.assertEqual(obj.id, 6)
        self.assertEqual(obj.size, 5)

    def test_update_with_kwargs(self):
        """Testing the method update with kwargs"""
        obj = Square(3, 10, 10, 10)
        obj.update(id=11, size=5, x=9, y=12)
        self.assertEqual(obj.id, 11)
        self.assertEqual(obj.size, 5)
        self.assertEqual(obj.x, 9)
        self.assertEqual(obj.y, 12)
        obj.update(size=30, x=10, y=2)
        self.assertEqual(obj.id, 11)
        self.assertEqual(obj.size, 30)
        self.assertEqual(obj.x, 10)
        self.assertEqual(obj.y, 2)

    def test_update_with_dictionnary(self):
        """Testing the method update with dictionary"""
        obj = Square(3, 10, 10, 10)
        obj.update(**{'id': 89})
        self.assertEqual(obj.id, 89)
        obj.update(**{'id': 89, 'size': 1})
        self.assertEqual(obj.id, 89)
        self.assertEqual(obj.size, 1)
        obj.update(**{'id': 89, 'size': 2})
        self.assertEqual(obj.id, 89)
        self.assertEqual(obj.size, 2)
        obj.update(**{'id': 89, 'size': 2, 'x': 3})
        self.assertEqual(obj.id, 89)
        self.assertEqual(obj.size, 2)
        self.assertEqual(obj.x, 3)
        obj.update(**{'id': 89, 'size': 2, 'x': 3, 'y': 4})
        self.assertEqual(obj.id, 89)
        self.assertEqual(obj.size, 2)
        self.assertEqual(obj.x, 3)
        self.assertEqual(obj.y, 4)

    def test_to_dictionary(self):
        """Testing the method to_dictionary"""
        obj = Square(10, 2, 1, 9)
        output = obj.to_dictionary()
        self.assertIsInstance(output, dict)
