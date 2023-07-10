#!/usr/bin/python3
import importlib.util

lookup_path = './100-my_int.py'

spec = importlib.util.spec_from_file_location('MyInt', lookup_path)
lookup_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lookup_module)

my_i = lookup_module.MyInt(3)
print(my_i)
print(my_i == 3)
print(my_i != 3)
