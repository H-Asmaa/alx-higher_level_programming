#!/usr/bin/python3
import importlib.util

lookup_path = './4-inherits_from.py'

spec = importlib.util.spec_from_file_location('inherits_from', lookup_path)
lookup_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lookup_module)
inherits_from = lookup_module.inherits_from

a = True
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))
if inherits_from(a, bool):
    print("{} inherited from class {}".format(a, bool.__name__))
if inherits_from(a, object):
    print("{} inherited from class {}".format(a, object.__name__))
