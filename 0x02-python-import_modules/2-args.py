#!/usr/bin/python3
import sys


def main():
    argv = sys.argv
    print("{} argument".format(len(argv) - 1), end="")
    if len(argv) == 1:
        print("s.")
    else:
        print(":")
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))


if __name__ == "__main__":
    main()

