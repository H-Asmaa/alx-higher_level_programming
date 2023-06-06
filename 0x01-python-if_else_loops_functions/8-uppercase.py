#!/usr/bin/python3
def uppercase(str_):
    for i in str_:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            print("{}".format(chr(ord(i) - 32)), end="")
        else:
            print("{}".format(i), end="")
    print("")
