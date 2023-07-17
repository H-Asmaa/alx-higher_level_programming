"""
	0x0C. Python - Almost a circle
"""
import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_id(self):
        obj_base = Base()
        self.assertIsInstance(obj_base, Base)
    """
    def test_to_json_string(self):
    def test_save_to_file(self):
    def test_from_json_string(self):
    def test_create(self):
    def test_load_from_file(self):
	"""


if __name__ == "__main__":
    unittest.main()
