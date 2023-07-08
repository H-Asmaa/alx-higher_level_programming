#!/usr/bin/python3
"""text_indentation function"""


def text_indentation(text):
    """
    Function that prints a text with 2 new lines after each of
    these characters: ., ? and :.

    Returns :
        Nothing

    Raises :
        TypeError in case the text is not string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in text:
        if i == "." or i == "?" or i == ":":
            print("{}\n".format(i))
        else:
            print("{}".format(i), end="")
