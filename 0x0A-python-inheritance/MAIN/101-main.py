#!/usr/bin/python3
import importlib.util

lookup_path = './101-add_attribute.py'

spec = importlib.util.spec_from_file_location('add_attribute', lookup_path)
lookup_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lookup_module)
add_attribute = lookup_module.add_attribute


class MyClass():
    pass

mc = MyClass()
add_attribute(mc, "name", "John")
print(mc.name)

try:
    a = "My String"
    add_attribute(a, "name", "Bob")
    print(a.name)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
