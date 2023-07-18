#!/usr/bin/python3
""" 3-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    """
        0)
        Main from Task.
        Expected output :                    |        Got:
        -------------------------------------------------------------------------------
        [TypeError] height must be an integer|  [TypeError] height must be an integer
        [ValueError] width must be > 0       |  [ValueError] width must be > 0
        [TypeError] x must be an integer     |  [TypeError] x must be an integer
        [ValueError] y must be >= 0          |  [ValueError] y must be >= 0
    """
    try:
        Rectangle(10, "2")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(10, 2)
        r.width = -10
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(10, 2)
        r.x = {}
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        Rectangle(10, 2, 3, -1)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    """
        1)
        Main from QA.
        Expected output = OK
        Got = OK
    """
    try:
        Rectangle("12", 13)
        print("TypeError exception not raised")
        exit(1)
    except TypeError as e:
        if str(e) != "width must be an integer":
            print("Wrong exception message: {}".format(e))
            exit(1)
    except Exception as e:
        print("Wrong exception: [{}] {}".format(type(e), e))
        exit(1)

    try:
        Rectangle([13], 13)
        print("TypeError exception not raised")
        exit(1)
    except TypeError as e:
        if str(e) != "width must be an integer":
            print("Wrong exception message: {}".format(e))
            exit(1)
    except Exception as e:
        print("Wrong exception: [{}] {}".format(type(e), e))
        exit(1)

    try:
        Rectangle(13.12, 13)
        print("TypeError exception not raised")
        exit(1)
    except TypeError as e:
        if str(e) != "width must be an integer":
            print("Wrong exception message: {}".format(e))
            exit(1)
    except Exception as e:
        print("Wrong exception: [{}] {}".format(type(e), e))
        exit(1)

    try:
        Rectangle({'id': 12}, 13)
        print("TypeError exception not raised")
        exit(1)
    except TypeError as e:
        if str(e) != "width must be an integer":
            print("Wrong exception message: {}".format(e))
            exit(1)
    except Exception as e:
        print("Wrong exception: [{}] {}".format(type(e), e))
        exit(1)

    print("OK", end="")

    """
        2)
        Main from QA.
        Expected output = OK
        Got = OK
    """
    try:
        Rectangle(13, "12")
        print("TypeError exception not raised")
        exit(1)
    except TypeError as e:
        if str(e) != "height must be an integer":
            print("Wrong exception message: {}".format(e))
            exit(1)
    except Exception as e:
        print("Wrong exception: [{}] {}".format(type(e), e))
        exit(1)

    try:
        Rectangle(13, [13])
        print("TypeError exception not raised")
        exit(1)
    except TypeError as e:
        if str(e) != "height must be an integer":
            print("Wrong exception message: {}".format(e))
            exit(1)
    except Exception as e:
        print("Wrong exception: [{}] {}".format(type(e), e))
        exit(1)

    try:
        Rectangle(13, 13.12)
        print("TypeError exception not raised")
        exit(1)
    except TypeError as e:
        if str(e) != "height must be an integer":
            print("Wrong exception message: {}".format(e))
            exit(1)
    except Exception as e:
        print("Wrong exception: [{}] {}".format(type(e), e))
        exit(1)

    try:
        Rectangle(13, {'id': 12})
        print("TypeError exception not raised")
        exit(1)
    except TypeError as e:
        if str(e) != "height must be an integer":
            print("Wrong exception message: {}".format(e))
            exit(1)
    except Exception as e:
        print("Wrong exception: [{}] {}".format(type(e), e))
        exit(1)

    print("OK", end="")

    """
        3)
        Main from QA.
        Expected output = OK
        Got = OK
    """
    try:
        Rectangle(13, 10, 1, "12")
        print("TypeError exception not raised")
        exit(1)
    except TypeError as e:
        if str(e) != "y must be an integer":
            print("Wrong exception message: {}".format(e))
            exit(1)
    except Exception as e:
        print("Wrong exception: [{}] {}".format(type(e), e))
        exit(1)

    try:
        Rectangle(13, 10, 1, [13])
        print("TypeError exception not raised")
        exit(1)
    except TypeError as e:
        if str(e) != "y must be an integer":
            print("Wrong exception message: {}".format(e))
            exit(1)
    except Exception as e:
        print("Wrong exception: [{}] {}".format(type(e), e))
        exit(1)

    try:
        Rectangle(13, 10, 1, 13.12)
        print("TypeError exception not raised")
        exit(1)
    except TypeError as e:
        if str(e) != "y must be an integer":
            print("Wrong exception message: {}".format(e))
            exit(1)
    except Exception as e:
        print("Wrong exception: [{}] {}".format(type(e), e))
        exit(1)

    try:
        Rectangle(13, 10, 1, {'id': 12})
        print("TypeError exception not raised")
        exit(1)
    except TypeError as e:
        if str(e) != "y must be an integer":
            print("Wrong exception message: {}".format(e))
            exit(1)
    except Exception as e:
        print("Wrong exception: [{}] {}".format(type(e), e))
        exit(1)

    print("OK", end="")

    """
        4)
        Main from QA.
        Expected output = OK
        Got = OK
    """
    r = Rectangle(10, 12)

    try:
        r.width = "12"
        print("TypeError exception not raised")
        exit(1)
    except TypeError as e:
        if str(e) != "width must be an integer":
            print("Wrong exception message: {}".format(e))
            exit(1)
    except Exception as e:
        print("Wrong exception: [{}] {}".format(type(e), e))
        exit(1)

    try:
        r.width = [13]
        print("TypeError exception not raised")
        exit(1)
    except TypeError as e:
        if str(e) != "width must be an integer":
            print("Wrong exception message: {}".format(e))
            exit(1)
    except Exception as e:
        print("Wrong exception: [{}] {}".format(type(e), e))
        exit(1)

    try:
        r.width = 13.12
        print("TypeError exception not raised")
        exit(1)
    except TypeError as e:
        if str(e) != "width must be an integer":
            print("Wrong exception message: {}".format(e))
            exit(1)
    except Exception as e:
        print("Wrong exception: [{}] {}".format(type(e), e))
        exit(1)

    try:
        r.width = {'id': 12}
        print("TypeError exception not raised")
        exit(1)
    except TypeError as e:
        if str(e) != "width must be an integer":
            print("Wrong exception message: {}".format(e))
            exit(1)
    except Exception as e:
        print("Wrong exception: [{}] {}".format(type(e), e))
        exit(1)

    print("OK", end="")

    """
        5)
        Main from QA.
        Expected output = OK
        Got = OK
    """
    r = Rectangle(10, 12)

    try:
        r.height = "12"
        print("TypeError exception not raised")
        exit(1)
    except TypeError as e:
        if str(e) != "height must be an integer":
            print("Wrong exception message: {}".format(e))
            exit(1)
    except Exception as e:
        print("Wrong exception: [{}] {}".format(type(e), e))
        exit(1)

    try:
        r.height = [13]
        print("TypeError exception not raised")
        exit(1)
    except TypeError as e:
        if str(e) != "height must be an integer":
            print("Wrong exception message: {}".format(e))
            exit(1)
    except Exception as e:
        print("Wrong exception: [{}] {}".format(type(e), e))
        exit(1)

    try:
        r.height = 13.12
        print("TypeError exception not raised")
        exit(1)
    except TypeError as e:
        if str(e) != "height must be an integer":
            print("Wrong exception message: {}".format(e))
            exit(1)
    except Exception as e:
        print("Wrong exception: [{}] {}".format(type(e), e))
        exit(1)

    try:
        r.height = {'id': 12}
        print("TypeError exception not raised")
        exit(1)
    except TypeError as e:
        if str(e) != "height must be an integer":
            print("Wrong exception message: {}".format(e))
            exit(1)
    except Exception as e:
        print("Wrong exception: [{}] {}".format(type(e), e))
        exit(1)

    print("OK", end="")

    """
        6)
        Main from QA.
        Expected output = OK
        Got = OK
    """
    r = Rectangle(10, 12)

    try:
        r.x = "12"
        print("TypeError exception not raised")
        exit(1)
    except TypeError as e:
        if str(e) != "x must be an integer":
            print("Wrong exception message: {}".format(e))
            exit(1)
    except Exception as e:
        print("Wrong exception: [{}] {}".format(type(e), e))
        exit(1)

    try:
        r.x = [13]
        print("TypeError exception not raised")
        exit(1)
    except TypeError as e:
        if str(e) != "x must be an integer":
            print("Wrong exception message: {}".format(e))
            exit(1)
    except Exception as e:
        print("Wrong exception: [{}] {}".format(type(e), e))
        exit(1)

    try:
        r.x = 13.12
        print("TypeError exception not raised")
        exit(1)
    except TypeError as e:
        if str(e) != "x must be an integer":
            print("Wrong exception message: {}".format(e))
            exit(1)
    except Exception as e:
        print("Wrong exception: [{}] {}".format(type(e), e))
        exit(1)

    try:
        r.x = {'id': 12}
        print("TypeError exception not raised")
        exit(1)
    except TypeError as e:
        if str(e) != "x must be an integer":
            print("Wrong exception message: {}".format(e))
            exit(1)
    except Exception as e:
        print("Wrong exception: [{}] {}".format(type(e), e))
        exit(1)

    print("OK", end="")

    """
        7)
        Main from QA.
        Expected output = OK
        Got = OK
    """
    r = Rectangle(10, 12)

    try:
        r.y = "12"
        print("TypeError exception not raised")
        exit(1)
    except TypeError as e:
        if str(e) != "y must be an integer":
            print("Wrong exception message: {}".format(e))
            exit(1)
    except Exception as e:
        print("Wrong exception: [{}] {}".format(type(e), e))
        exit(1)

    try:
        r.y = [13]
        print("TypeError exception not raised")
        exit(1)
    except TypeError as e:
        if str(e) != "y must be an integer":
            print("Wrong exception message: {}".format(e))
            exit(1)
    except Exception as e:
        print("Wrong exception: [{}] {}".format(type(e), e))
        exit(1)

    try:
        r.y = 13.12
        print("TypeError exception not raised")
        exit(1)
    except TypeError as e:
        if str(e) != "y must be an integer":
            print("Wrong exception message: {}".format(e))
            exit(1)
    except Exception as e:
        print("Wrong exception: [{}] {}".format(type(e), e))
        exit(1)

    try:
        r.y = {'id': 12}
        print("TypeError exception not raised")
        exit(1)
    except TypeError as e:
        if str(e) != "y must be an integer":
            print("Wrong exception message: {}".format(e))
            exit(1)
    except Exception as e:
        print("Wrong exception: [{}] {}".format(type(e), e))
        exit(1)

    print("OK", end="")

    """
        8)
        Main from QA.
        Expected output = OK
        Got = OK
    """
    try:
        Rectangle(-12, 13)
        print("ValueError exception not raised")
        exit(1)
    except ValueError as e:
        if str(e) != "width must be > 0":
            print("Wrong exception message: {}".format(e))
            exit(1)
    except Exception as e:
        print("Wrong exception: [{}] {}".format(type(e), e))
        exit(1)

    try:
        Rectangle(-89, 13)
        print("ValueError exception not raised")
        exit(1)
    except ValueError as e:
        if str(e) != "width must be > 0":
            print("Wrong exception message: {}".format(e))
            exit(1)
    except Exception as e:
        print("Wrong exception: [{}] {}".format(type(e), e))
        exit(1)

    try:
        Rectangle(0, 13)
        print("ValueError exception not raised")
        exit(1)
    except ValueError as e:
        if str(e) != "width must be > 0":
            print("Wrong exception message: {}".format(e))
            exit(1)
    except Exception as e:
        print("Wrong exception: [{}] {}".format(type(e), e))
        exit(1)

    print("OK", end="")

    """
        9)
        Main from QA.
        Expected output = OK
        Got = OK
    """
    try:
        Rectangle(12, -13)
        print("ValueError exception not raised")
        exit(1)
    except ValueError as e:
        if str(e) != "height must be > 0":
            print("Wrong exception message: {}".format(e))
            exit(1)
    except Exception as e:
        print("Wrong exception: [{}] {}".format(type(e), e))
        exit(1)

    try:
        Rectangle(13, -89)
        print("ValueError exception not raised")
        exit(1)
    except ValueError as e:
        if str(e) != "height must be > 0":
            print("Wrong exception message: {}".format(e))
            exit(1)
    except Exception as e:
        print("Wrong exception: [{}] {}".format(type(e), e))
        exit(1)

    try:
        Rectangle(13, 0)
        print("ValueError exception not raised")
        exit(1)
    except ValueError as e:
        if str(e) != "height must be > 0":
            print("Wrong exception message: {}".format(e))
            exit(1)
    except Exception as e:
        print("Wrong exception: [{}] {}".format(type(e), e))
        exit(1)

    print("OK", end="")

    """
        10)
        Main from QA.
        Expected output = OK
        Got = OK
    """
    try:
        Rectangle(12, 13, -12)
        print("ValueError exception not raised")
        exit(1)
    except ValueError as e:
        if str(e) != "x must be >= 0":
            print("Wrong exception message: {}".format(e))
            exit(1)
    except Exception as e:
        print("Wrong exception: [{}] {}".format(type(e), e))
        exit(1)

    try:
        Rectangle(12, 13, -89)
        print("ValueError exception not raised")
        exit(1)
    except ValueError as e:
        if str(e) != "x must be >= 0":
            print("Wrong exception message: {}".format(e))
            exit(1)
    except Exception as e:
        print("Wrong exception: [{}] {}".format(type(e), e))
        exit(1)

    try:
        Rectangle(12, 13, -1)
        print("ValueError exception not raised")
        exit(1)
    except ValueError as e:
        if str(e) != "x must be >= 0":
            print("Wrong exception message: {}".format(e))
            exit(1)
    except Exception as e:
        print("Wrong exception: [{}] {}".format(type(e), e))
        exit(1)

    try:
        Rectangle(12, 13, 0)
        print("OK", end="")
    except Exception as e:
        print("0 is valid for x: [{}] {}".format(type(e), e))
        exit(1)

    """
        11)
        Main from QA.
        Expected output = OK
        Got = OK
    """
    try:
        Rectangle(12, 13, 1, -12)
        print("ValueError exception not raised")
        exit(1)
    except ValueError as e:
        if str(e) != "y must be >= 0":
            print("Wrong exception message: {}".format(e))
            exit(1)
    except Exception as e:
        print("Wrong exception: [{}] {}".format(type(e), e))
        exit(1)

    try:
        Rectangle(12, 13, 1, -89)
        print("ValueError exception not raised")
        exit(1)
    except ValueError as e:
        if str(e) != "y must be >= 0":
            print("Wrong exception message: {}".format(e))
            exit(1)
    except Exception as e:
        print("Wrong exception: [{}] {}".format(type(e), e))
        exit(1)

    try:
        Rectangle(12, 13, 1, -1)
        print("ValueError exception not raised")
        exit(1)
    except ValueError as e:
        if str(e) != "y must be >= 0":
            print("Wrong exception message: {}".format(e))
            exit(1)
    except Exception as e:
        print("Wrong exception: [{}] {}".format(type(e), e))
        exit(1)

    try:
        Rectangle(12, 13, 1, 0)
        print("OK", end="")
    except Exception as e:
        print("0 is valid for y: [{}] {}".format(type(e), e))
        exit(1)

    """
        12)
        Main from QA.
        Expected output = OK
        Got = OK
    """
    r = Rectangle(10, 12)

    try:
        r.width = -12
        print("ValueError exception not raised")
        exit(1)
    except ValueError as e:
        if str(e) != "width must be > 0":
            print("Wrong exception message: {}".format(e))
            exit(1)
    except Exception as e:
        print("Wrong exception: [{}] {}".format(type(e), e))
        exit(1)

    try:
        r.width = -89
        print("ValueError exception not raised")
        exit(1)
    except ValueError as e:
        if str(e) != "width must be > 0":
            print("Wrong exception message: {}".format(e))
            exit(1)
    except Exception as e:
        print("Wrong exception: [{}] {}".format(type(e), e))
        exit(1)

    try:
        r.width = 0
        print("ValueError exception not raised")
        exit(1)
    except ValueError as e:
        if str(e) != "width must be > 0":
            print("Wrong exception message: {}".format(e))
            exit(1)
    except Exception as e:
        print("Wrong exception: [{}] {}".format(type(e), e))
        exit(1)

    print("OK", end="")

    """
        13)
        Main from QA.
        Expected output = OK
        Got = OK
    """
    r = Rectangle(10, 12)

    try:
        r.height = -12
        print("ValueError exception not raised")
        exit(1)
    except ValueError as e:
        if str(e) != "height must be > 0":
            print("Wrong exception message: {}".format(e))
            exit(1)
    except Exception as e:
        print("Wrong exception: [{}] {}".format(type(e), e))
        exit(1)

    try:
        r.height = -89
        print("ValueError exception not raised")
        exit(1)
    except ValueError as e:
        if str(e) != "height must be > 0":
            print("Wrong exception message: {}".format(e))
            exit(1)
    except Exception as e:
        print("Wrong exception: [{}] {}".format(type(e), e))
        exit(1)

    try:
        r.height = 0
        print("ValueError exception not raised")
        exit(1)
    except ValueError as e:
        if str(e) != "height must be > 0":
            print("Wrong exception message: {}".format(e))
            exit(1)
    except Exception as e:
        print("Wrong exception: [{}] {}".format(type(e), e))
        exit(1)

    print("OK", end="")

    """
        14)
        Main from QA.
        Expected output = OK
        Got = OK
    """
    r = Rectangle(10, 12)

    try:
        r.x = -12
        print("ValueError exception not raised")
        exit(1)
    except ValueError as e:
        if str(e) != "x must be >= 0":
            print("Wrong exception message: {}".format(e))
            exit(1)
    except Exception as e:
        print("Wrong exception: [{}] {}".format(type(e), e))
        exit(1)

    try:
        r.x = -89
        print("ValueError exception not raised")
        exit(1)
    except ValueError as e:
        if str(e) != "x must be >= 0":
            print("Wrong exception message: {}".format(e))
            exit(1)
    except Exception as e:
        print("Wrong exception: [{}] {}".format(type(e), e))
        exit(1)

    try:
        r.x = -1
        print("ValueError exception not raised")
        exit(1)
    except ValueError as e:
        if str(e) != "x must be >= 0":
            print("Wrong exception message: {}".format(e))
            exit(1)
    except Exception as e:
        print("Wrong exception: [{}] {}".format(type(e), e))
        exit(1)

    try:
        r.x = 0
        print("OK", end="")
    except Exception as e:
        print("0 is valid for x: [{}] {}".format(type(e), e))
        exit(1)

    """
        15)
        Main from QA.
        Expected output = OK
        Got = OK
    """
    r = Rectangle(10, 12)

    try:
        r.y = -12
        print("ValueError exception not raised")
        exit(1)
    except ValueError as e:
        if str(e) != "y must be >= 0":
            print("Wrong exception message: {}".format(e))
            exit(1)
    except Exception as e:
        print("Wrong exception: [{}] {}".format(type(e), e))
        exit(1)

    try:
        r.y = -89
        print("ValueError exception not raised")
        exit(1)
    except ValueError as e:
        if str(e) != "y must be >= 0":
            print("Wrong exception message: {}".format(e))
            exit(1)
    except Exception as e:
        print("Wrong exception: [{}] {}".format(type(e), e))
        exit(1)

    try:
        r.y = -1
        print("ValueError exception not raised")
        exit(1)
    except ValueError as e:
        if str(e) != "y must be >= 0":
            print("Wrong exception message: {}".format(e))
            exit(1)
    except Exception as e:
        print("Wrong exception: [{}] {}".format(type(e), e))
        exit(1)

    try:
        r.y = 0
        print("OK", end="")
    except Exception as e:
        print("0 is valid for y: [{}] {}".format(type(e), e))
        exit(1)
