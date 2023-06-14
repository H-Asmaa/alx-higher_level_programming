#!/usr/bin/python3
def best_score(a_dictionary):
    max_value = 0
    for key in a_dictionary:
        if a_dictionary[key] > max_value:
            max_value = a_dictionary[key]
    return max_value
