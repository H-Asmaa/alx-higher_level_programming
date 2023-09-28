#!/usr/bin/python3
# A script that finds the peak


def find_peak(list_of_integers):
    """A function that returns the peak"""
    for i in range(1, len(list_of_integers) - 1):
        prev = list_of_integers[i - 1]
        follow = list_of_integers[i + 1]
        curr = list_of_integers[i]
        if curr > prev and curr > follow:
            return curr
    i = list_of_integers
    if (len(i)) >= 2 and i[0] >= i[1]:
        return i[0]
    if (len(i)) >= 2 and i[-2] <= i[-1]:
        return i[-1]
    return None
