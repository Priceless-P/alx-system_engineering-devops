#!/usr/bin/python3
"""
Python script that sends a request to the URL and
displays the body of the response (decoded in utf-8).
"""

import sys
import requests


url = sys.argv[1]

response = requests.get(url)

if response.ok:
    print(response.text)
else:
    print("Error code: {}".format(response.status_code))
