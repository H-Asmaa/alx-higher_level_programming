#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    list_1 = list(map(lambda x: x, filter(lambda x: x not in set_1, set_2)))
    list_2 = list(map(lambda x: x, filter(lambda x: x not in set_2, set_1)))
    return list_1 + list_2
