"""
0x0C. Python - Almost a circle
"""
from models.base import Base
from models.rectangle import Rectangle
import unittest


class TestBase(unittest.TestCase):
    """
        All your files, classes and methods must be unit tested
        and be PEP 8 validated.
        command : python3 -m unittest discover tests
    """

    def test_to_dictionary(self):
        """Testing the method to_dictionary"""
        obj = Rectangle(10, 2, 1, 9)
        output = obj.to_dictionary()
        self.assertIsInstance(output, dict)
