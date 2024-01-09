#!/usr/bin/python3
"""
Python script that sends a POST request to URL with
email as a parameter, and displays the body of the
response (decoded in utf-8)
"""
import sys
import requests


url = sys.argv[1]
email = sys.argv[2]
data = {'email': email}

body = requests.post(url, data=data)
print(body.text)
