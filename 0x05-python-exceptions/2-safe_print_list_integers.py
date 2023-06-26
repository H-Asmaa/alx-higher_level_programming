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


"""
def safe_print_list_integers(my_list=[], x=0):
    for i in range(0, x):
        if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")




def safe_print_list_integers(my_list=[], x=0):
    try:
        current = 0
        L = []
        for i in my_list:
            if isinstance(i, int):
                L.append(i)
                current += 1
        for i in range(0, x):
            print("{:d}".format(L[i]), end="")
        return (current)
    except IndexError:
        print("ERROR")"""


my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))
