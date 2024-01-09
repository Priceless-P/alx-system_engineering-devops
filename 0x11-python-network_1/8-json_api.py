#!/usr/bin/python3
"""
Python script that takes in a letter and
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import sys
import requests

url = "http://0.0.0.0:5000/search_user"
if len(sys.argv) > 1:
    q = sys.argv[1]
else:
    q = ""
params = {'q': q}

response = requests.post(url, params=params)

try:
    response_json = response.json()
    if response_json:
        print("[{}] {}".format(response_json['id'], response_json['name']))
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
