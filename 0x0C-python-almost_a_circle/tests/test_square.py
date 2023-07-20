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
