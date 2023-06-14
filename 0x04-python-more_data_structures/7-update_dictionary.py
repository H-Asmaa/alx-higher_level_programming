#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for key_search in a_dictionary:
        if key_search == key:
            a_dictionary[key] = value
    return (a_dictionary)
def print_sorted_dictionary(a_dictionary):
    for key, val in sorted(a_dictionary.items()):
        print("{}: {}".format(key, val))
