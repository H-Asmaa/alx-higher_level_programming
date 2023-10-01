#!/usr/bin/python3
"""A script that fetches https://alx-intranet.hbtn.io/status"""

if __name__ == "__main__":
    import urllib.request as ulib

    with ulib.urlopen('https://alx-intranet.hbtn.io/status') as response:
        content = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
    print("\t- utf8 content: {}".format(content.decode("UTF-8")))
