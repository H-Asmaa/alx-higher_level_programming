#!/usr/bin/python3
def remove_char_at(str, n):
    str_tmp = ""
    if n < 0:
        return str
    for i in range(0, len(str)):
        if i != n:
            str_tmp += str[i]
    return str_tmp
