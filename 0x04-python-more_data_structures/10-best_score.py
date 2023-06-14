#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_value = float('-inf')
    max_key = None
    for key, val in a_dictionary.items():
        if val > max_value:
            max_value = val
            max_key = key
    return max_key
