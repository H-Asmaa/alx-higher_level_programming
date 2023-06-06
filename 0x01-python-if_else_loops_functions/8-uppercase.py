#!/usr/bin/python3
def uppercase(str_):
    for i in str_:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            tmp = chr(ord(i) - 32)
        else:
            tmp = i
        print("{}".format(tmp), end="")
    print("")
