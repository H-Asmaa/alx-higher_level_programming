#!/usr/bin/python3
import importlib.util

lookup_path = './6-base_geometry.py'

spec = importlib.util.spec_from_file_location('BaseGeometry', lookup_path)
lookup_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lookup_module)
BaseGeometry = lookup_module.BaseGeometry

bg = BaseGeometry()

try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
