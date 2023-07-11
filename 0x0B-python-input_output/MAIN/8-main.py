#!/usr/bin/python3
import importlib.util

lookup_path = './8-my_class_2.py'

spec = importlib.util.spec_from_file_location('MyClass', lookup_path)
lookup_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lookup_module)
MyClass = lookup_module.MyClass

lookup_path = './8-class_to_json.py'

spec = importlib.util.spec_from_file_location('class_to_json', lookup_path)
lookup_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lookup_module)
class_to_json = lookup_module.class_to_json

m = MyClass("John")
m.win()
print(type(m))
print(m)

mj = class_to_json(m)
print(type(mj))
print(mj)
