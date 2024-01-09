#!/usr/bin/python3
"""
Python script that sends a request to URL and displays the value
of the X-Request-Id variable found in the header
"""
import sys
import urllib.request


url = sys.argv[1]
req = urllib.request.Request(url)

with urllib.request.urlopen(req) as response:
    print(response.info()['X-Request-Id'])
