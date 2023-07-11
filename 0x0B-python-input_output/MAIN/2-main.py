#!/usr/bin/python3
import importlib.util

lookup_path = './2-append_write.py'

spec = importlib.util.spec_from_file_location('append_write', lookup_path)
lookup_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lookup_module)
append_write = lookup_module.append_write

nb_characters_added = append_write("file_append.txt", "This School is so cool!\n")
print(nb_characters_added)
