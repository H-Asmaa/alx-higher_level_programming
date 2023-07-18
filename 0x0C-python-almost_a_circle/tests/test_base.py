"""
	0x0C. Python - Almost a circle
"""
from models.base import Base
from models.rectangle import Rectangle
import unittest
import os


class TestBase(unittest.TestCase):
    def test_id(self):
        obj_base = Base()
        self.assertIsInstance(obj_base, Base)
        obj_base.id = 2
        self.assertEqual(obj_base.id, 2)
        obj_base.id = 3
        self.assertEqual(obj_base.id, 3)

    def test_to_json_string(self):
        obj_base = Base()
        json_str = obj_base.to_json_string({'x': 2,
                                            'width': 10,
                                            'id': 1,
                                            'height': 7,
                                            'y': 8})
        expected_str = '{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}'
        self.assertIsInstance(json_str, str)
        self.assertEqual(json_str, expected_str)
        json_str = obj_base.to_json_string(None)
        self.assertIsInstance(json_str, str)

    def test_from_json_string(self):
        list_input = [{'height': 2, 'width': 1, 'id': 77},
                      {'height': 18, 'width': 11, 'id': 7}]
        json_str = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_str)
        self.assertEqual(list_output, list_input)
        self.assertIsInstance(list_output, list)

        list_input = [{'height': 2, 'width': 1, 'id': 77},
                      {'height': 18, 'width': 11, 'id': 7}]
        json_str = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_str)
        self.assertEqual(list_output, [{'height': 4, 'width': 10, 'id': 89,
                                        'x': 3, 'y': 2},
                                       {'height': 7, 'width': 1, 'id': 7,
                                        'x': 3}])
        self.assertIsInstance(list_output, list)


"""
    def test_save_to_file(self):
        obj_base = Base()
        obj_base.save_to_file(Base, {'x': 2,
                                     'width': 10,
                                     'id': 1,
                                     'height': 7,
                                     'y': 8})
        with open("Base.json", "r") as file:
            file_content = file.read()
        self.assertEqual(file_content, {'x': 2,
                                        'width': 10,
                                        'id': 1,
                                        'height': 7,
                                        'y': 8})

    def test_create(self):
    def test_load_from_file(self):
	"""


if __name__ == "__main__":
    unittest.main()
