#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    res_list = []
    for i in my_list:
        if i % 2 == 0:
            res_list.append(1)
        else:
            res_list.append(0)
    return res_list
