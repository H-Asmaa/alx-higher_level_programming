#!/usr/bin/python3
for i in range(25, -1, -1):
    print("{}".format(chr(i + 97)).upper() if i %
          2 == 0 else "{}".format(chr(i + 97)), end="")
