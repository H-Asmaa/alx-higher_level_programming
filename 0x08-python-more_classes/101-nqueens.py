#!/usr/bin/python3
import sys


def chessboard(n):
    board = []
    for i in range(n):
        row = [0] * n
        board.append(row)
    return board


argv = sys.argv

if len(argv) > 2:
    print("{}".format("Usage: nqueens N"))
    exit(1)
if not argv[1].isdigit():
    print("{}".format("N must be a number"))
    exit(1)
argv = int(argv[1])
if argv < 4:
    print("{}".format("N must be at least 4"))
    exit(1)
