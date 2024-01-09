#!/usr/bin/python3
""""
Python script that fetches https://alx-intranet.hbtn.io/status
"""""
import requests


url = "https://alx-intranet.hbtn.io/status"
page = requests.get(url)
print("Body response:")
print("\t- type:", type(page.text))
print("\t- content:", page.text)
