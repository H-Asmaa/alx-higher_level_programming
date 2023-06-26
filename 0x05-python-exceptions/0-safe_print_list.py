#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        j = 0
        for i in my_list:
            j += 1
        if x > j:
            for i in my_list:
                print("{}".format(i), end="")
        else:
            j = x
            for i in range(0, x):
                print("{}".format(my_list[i]), end="")
        print("")
    except ValueError:
        pass
    return (j)
