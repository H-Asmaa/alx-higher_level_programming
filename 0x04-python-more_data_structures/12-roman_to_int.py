#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_val = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    number = 0
    prev_value = 0
    for char in roman_string:
        value = roman_val[char]
        if value > prev_value:
            number += value - 2 * prev_value
        else:
            number += value
        prev_value = value
    return number
