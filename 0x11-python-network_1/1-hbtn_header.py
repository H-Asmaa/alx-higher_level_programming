#!/usr/bin/python3
"""A script that takes in a URL, sends a request to the
URL and displays the value of the X-Request-Id variable
found in the header of the response."""
import sys
import urllib.request as ulib

if __name__ == "__main__":
    with ulib.urlopen(sys.argv[1]) as response:
        request_id = response.getheader("X-Request-Id")
        print("{}".format(request_id))
