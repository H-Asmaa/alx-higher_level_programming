#!/usr/bin/python3
"""A script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8)."""


if __name__ == "__main__":
    import urllib.request as ulib
    from sys import argv

    try:
        with ulib.urlopen(argv[1]) as response:
            content = response.read().decode("UTF-8")
            print("{}".format(content))
    except ulib.HTTPError as e:
        print("Error code: {}".format(e.code))
