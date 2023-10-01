#!/usr/bin/python3
"""A  script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays the
body of the response (decoded in utf-8)"""
import urllib.request as ulib
from sys import argv

if __name__ == "__main__":
    with ulib.urlopen(argv[1], data=argv[2].encode("UTF-8")) as response:
        content = response.read().decode("UTF-8")
        print(content)
