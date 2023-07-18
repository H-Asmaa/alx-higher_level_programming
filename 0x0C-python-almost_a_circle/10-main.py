#!/usr/bin/python3
""" 10-main """
from models.square import Square

if __name__ == "__main__":

    s1 = Square(5)
    print(s1)
    print(s1.area())
    s1.display()

    print("---")

    s2 = Square(2, 2)
    print(s2)
    print(s2.area())
    s2.display()

    print("---")

    s3 = Square(3, 1, 3)
    print(s3)
    print(s3.area())
    s3.display()

    """
        Main from QA.
        Expected output = OK
        Got = OK
    """
    s = Square(5, 7, 2, 89)
    if s.id != 89:
        print("ID must be equal to 89: {}".format(s.id))
        exit(1)

    if s.width != 5:
        print("Width of the Square must be 5: {}".format(s.width))
        exit(1)

    if s.height != 5:
        print("Height of the Square must be 5: {}".format(s.height))
        exit(1)

    if s.x != 7:
        print("X of the Square must be 7: {}".format(s.x))
        exit(1)

    if s.y != 2:
        print("Y of the Square must be 2: {}".format(s.y))
        exit(1)

    print("OK", end="")
