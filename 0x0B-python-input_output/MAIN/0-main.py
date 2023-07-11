#!/usr/bin/python3
import importlib.util

lookup_path = './0-read_file.py'

spec = importlib.util.spec_from_file_location('read_file', lookup_path)
lookup_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lookup_module)
read_file = lookup_module.read_file

read_file("my_file_0.txt")
