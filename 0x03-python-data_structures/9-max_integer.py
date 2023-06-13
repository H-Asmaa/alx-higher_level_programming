#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    sorted_list = my_list.copy()
    for i in range(len(sorted_list)):
        for j in range(0, len(sorted_list) - i - 1):
            if sorted_list[j] > sorted_list[j + 1]:
                tmp = sorted_list[j]
                sorted_list[j] = sorted_list[j + 1]
                sorted_list[j + 1] = tmp
    return sorted_list[-1]
