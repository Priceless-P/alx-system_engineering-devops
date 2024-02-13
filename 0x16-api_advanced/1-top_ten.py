#!/usr/bin/python3
"""
 Top Ten
"""
from markupsafe import escape
import requests


def top_ten(subreddit):
    """Queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit
    """

    url = "https://www.reddit.com/r/{}/hot.json".format(escape(subreddit))
    headers = {
        "User-Agent": "AppleWebKit:0x16.api.advanced:v1.0.0 \
                       (by /u/JazzlikeFig4018)"
    }
    params = {
        "limit": 10
    }
    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)

    if res.status_code == 404:
        return None
    results = res.json().get("data")
    for child in results.get("children"):
        print(child.get("data").get("title"))
