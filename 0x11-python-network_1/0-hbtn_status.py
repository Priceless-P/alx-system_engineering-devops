#!/usr/bin/python3
"""
Python script that fetches
https://alx-intranet.hbtn.io/status
"""
import urllib.request

url = "https://alx-intranet.hbtn.io/status"
req = urllib.request.Request(url)

with urllib.request.urlopen(req) as response:
    page = response.read()
    print("Body response:")
    print("\t- type:", type(page))
    print("\t- content:", page)
    print("\t- utf8 content:", page.decode('utf-8'))
