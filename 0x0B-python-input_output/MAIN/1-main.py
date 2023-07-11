#!/usr/bin/python3
import importlib.util

lookup_path = './1-write_file.py'

spec = importlib.util.spec_from_file_location('write_file', lookup_path)
lookup_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lookup_module)
write_file = lookup_module.write_file

nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)
