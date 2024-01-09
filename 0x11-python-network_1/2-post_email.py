#!/usr/bin/python3
"""
Python script that sends a POST request to URL with
email as a parameter, and displays the body of the
response (decoded in utf-8)
"""
import sys
import urllib.request
import urllib.parse


url = sys.argv[1]
email = sys.argv[2]
val = {'email': email}
data = urllib.parse.urlencode(val)
data = data.encode('ascii')

req = urllib.request.Request(url, data)

with urllib.request.urlopen(req) as response:
    res = response.read().decode('utf-8')
    print(res)
