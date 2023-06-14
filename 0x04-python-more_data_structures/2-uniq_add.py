#!/usr/bin/python3
def uniq_add(my_list):
    filtered_list = []
    sum = 0
    for i in range(len(my_list)):
        if my_list[i] not in filtered_list:
            filtered_list.append(my_list[i])
    for i in filtered_list:
        sum += i
    return sum
