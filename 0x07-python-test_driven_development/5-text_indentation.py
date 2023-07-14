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
    tmp = ""
    space = True
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            if i == len(text) - 1:
                tmp += text[i]
            else:
                tmp += text[i] + "\n\n"
            space = False
        elif text[i] == " " and space is False:
            continue
        else:
            tmp += text[i]
            space = True
    print("{}".format(tmp), end="")
