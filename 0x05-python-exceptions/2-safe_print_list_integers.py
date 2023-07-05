#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    L = []
    count = 0
    for i in range(x):
        try:
            if isinstance(my_list[i], int):
                L.append(my_list[i])
        except (ValueError, TypeError):
            continue
    for i in L:
        print("{:d}".format(i), end="")
        count += 1
    print()
    return count

my_list = []

nb_print = safe_print_list_integers(my_list, 0)
print("nb_print: {:d}".format(nb_print))
