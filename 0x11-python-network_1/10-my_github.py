#!/usr/bin/python3
"""
 Python script that takes your GitHub credentials
 (username and password) and uses the GitHub API to display your id
"""
import sys
import requests


url = "https://api.github.com/user"
username = sys.argv[1]
password = sys.argv[2]
header = {
    'Accept': "application/vnd.github+json",
    'X-GitHub-Api-Version': "2022-11-28"}

response = requests.get(url, headers=header, auth=(username, password))
print(response.json()['id'])
