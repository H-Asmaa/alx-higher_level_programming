"""
0x0C. Python - Almost a circle
"""
from models.base import Base
from models.rectangle import Rectangle
import unittest
import os


class TestBase(unittest.TestCase):
    """
        All your files, classes and methods must be unit tested
        and be PEP 8 validated.
        command : python3 -m unittest discover tests
    """

    def test_id(self):
        """Testing the attribute ID"""
        obj_base = Base()
        self.assertIsInstance(obj_base, Base)
        obj_base.id = 2
        self.assertEqual(obj_base.id, 2)
        obj_base.id = 3
        self.assertEqual(obj_base.id, 3)
        obj_base = Base(89)
        self.assertEqual(obj_base.id, 89)

    def test_to_json_string(self):
        """Testing the method to_json_string"""
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
        expected_str = '[]'
        self.assertEqual(json_str, expected_str)
        json_str = obj_base.to_json_string([])
        expected_str = '[]'
        self.assertEqual(json_str, expected_str)
        json_str = obj_base.to_json_string([{'id':12}])
        expected_str = '[{"id": 12}]'
        self.assertEqual(json_str, expected_str)

    def test_from_json_string(self):
        """Testing the method from_json_string"""
        list_input = [{'height': 2, 'width': 1, 'id': 77},
                      {'height': 18, 'width': 11, 'id': 7}]
        json_str = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_str)
        self.assertEqual(list_output, list_input)
        self.assertIsInstance(list_output, list)
        list_input = None
        json_str = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_str)
        self.assertEqual(list_output, [])
        list_input = []
        json_str = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_str)
        self.assertEqual(list_output, [])
        list_input = '[{ "id": 89 }]'
        json_str = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_str)
        self.assertEqual(list_output, '[{ "id": 89 }]')

    def test_create(self):
        """Testing the method create"""
        obj = Rectangle(3, 5, 1)
        obj_dict = obj.to_dictionary()
        obj_creation = Rectangle.create(**obj_dict)
        self.assertEqual("[Rectangle] (1) 1/0 - 3/5", str(obj_creation))
        obj_creation = Rectangle.create(**{'id': 89, 'width': 1, 'height': 3})
        self.assertEqual("[Rectangle] (89) 0/0 - 1/3", str(obj_creation))
        obj_creation = Rectangle.create(
            **{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual("[Rectangle] (89) 3/0 - 1/2", str(obj_creation))
        obj_creation = Rectangle.create(
            **{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual("[Rectangle] (89) 3/4 - 1/2", str(obj_creation))

if __name__ == "__main__":
    unittest.main()
