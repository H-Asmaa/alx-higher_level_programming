#!/usr/bin/python3
"""A script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""


if __name__ == "__main__":
    import requests
    from sys import argv

    q = argv[1]
    response = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})
    try:
        content = response.json()
        if (content):
            print("[{}] {}".format(content.get("id"), content.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
