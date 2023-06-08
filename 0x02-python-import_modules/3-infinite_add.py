#!/usr/bin/python3
import sys


def main():
    argv = sys.argv
    sum_all = 0
    for i in range(1, len(argv)):
        sum_all += int(argv[i])
    print("{}".format(sum_all))


if __name__ == "__main__":
    main()
