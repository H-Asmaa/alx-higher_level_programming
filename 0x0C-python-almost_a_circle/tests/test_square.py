"""
0x0C. Python - Almost a circle
"""
from models.base import Base
from models.square import Square
import unittest


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

    def test_to_dictionary(self):
        """Testing the method to_dictionary"""
        obj = Square(10, 2, 1, 9)
        output = obj.to_dictionary()
        self.assertIsInstance(output, dict)
