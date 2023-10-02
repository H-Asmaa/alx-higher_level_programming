#!/usr/bin/python3
"""A script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""


if __name__ == "__main__":
    from sys import argv
    import requests

    username = argv[1]
    password = argv[2]
    url = "https://api.github.com/user"
    info = {"login": argv[1]}
    response = requests.get(url, auth=(username, password), params=info).json()
    if response.get("id") is not None:
        print("{}".format(response.get("id")))
    else:
        print("None")
