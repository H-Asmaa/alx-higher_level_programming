#!/usr/bin/python3
"""A script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""


if __name__ == "__main__":
    import requests
    from sys import argv

    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""
    response = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})
    try:
        content = response.json()
        content_id = content.get("id", "")
        content_name = content.get("name", "")
        if content_id and content_name:
            print("[{}] {}".format(content_id, content_name))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
