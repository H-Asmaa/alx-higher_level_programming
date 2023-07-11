#!/usr/bin/python3
import importlib.util

lookup_path = './5-save_to_json_file.py'

spec = importlib.util.spec_from_file_location('save_to_json_file', lookup_path)
lookup_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lookup_module)
save_to_json_file = lookup_module.save_to_json_file


filename = "my_list.json"
my_list = [1, 2, 3]
save_to_json_file(my_list, filename)

filename = "my_dict.json"
my_dict = {
    'id': 12,
    'name': "John",
    'places': ["San Francisco", "Tokyo"],
    'is_active': True,
    'info': {
        'age': 36,
        'average': 3.14
    }
}
save_to_json_file(my_dict, filename)

try:
    filename = "my_set.json"
    my_set = {132, 3}
    save_to_json_file(my_set, filename)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
