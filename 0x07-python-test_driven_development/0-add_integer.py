#!/usr/bin/python3
def add_integer(a, b=98):
    """
    >>> add_integer(1, 2)
    3
    >>> add_integer(100, -2)
    98
    >>> add_integer(2)
    100
    >>> add_integer(100.3, -2)
    98
    >>> add_integer(4, "School")
    Traceback (most recent call last):
    ...
    TypeError: b must be an integer or float
    >>> add_integer("Hello", 7)
    Traceback (most recent call last):
    ...
    TypeError: a must be an integer or float
    >>> add_integer(None)
    98
    """
    if a is None:
        return int(b)
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    return int(a) + int(b)
