#!/usr/bin/python3
"""A  script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays the
body of the response (decoded in utf-8)"""


if __name__ == "__main__":
    import urllib
    import urllib.request as ulib
    from sys import argv

    data = urllib.parse.urlencode({"email": argv[2]}).encode("UTF-8")
    request = ulib.Request(argv[1], data)
    with ulib.urlopen(request, data) as response:
        content = response.read().decode("UTF-8")
        print("{}".format(content))
