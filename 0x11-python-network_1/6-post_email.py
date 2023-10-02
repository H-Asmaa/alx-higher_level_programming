#!/usr/bin/python3
"""A script that fetches https://alx-intranet.hbtn.io/status"""


if __name__ == "__main__":
    import requests
    from sys import argv

    response = requests.post(argv[1], data={"email": argv[2].encode("UTF-8")})
    print(response.text)
