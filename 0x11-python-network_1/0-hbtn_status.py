#!/usr/bin/python3
"""A script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request as ulib

content = ulib.urlopen("https://alx-intranet.hbtn.io/status")
content_read = content.read()
print("Body response:")
print("\t- type: {}".format(type(content_read)))
print("\t- content: {}".format(content_read))
print("\t- utf8 content: {}".format(content_read.decode("utf-8")))
