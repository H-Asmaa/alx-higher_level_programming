#!/usr/bin/python3
import sys


def main():
    argv = sys.argv
    for i in range(1, len(argv)):
        print("{} : {}".format(i, argv[i]))


if __name__ == "__main__":
    main()
