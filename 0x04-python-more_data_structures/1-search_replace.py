#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_list_copy = my_list.copy()
    for i in range(len(my_list_copy)):
        if my_list_copy[i] == search:
            my_list_copy[i] = replace
    return my_list_copy
