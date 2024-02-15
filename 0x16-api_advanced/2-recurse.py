#!/usr/bin/python3
"""
Recurse it!
This function queries a list of all
hot posts on a given Reddit subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit
    """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "AppleWebKit:0x16.api.advanced:v1.0.0 \
                       (by /u/JazzlikeFig4018)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)
    # list_ = []
    if res.status_code == 404:
        return None
    results = res.json().get("data")
    after = results.get("after")
    count += results.get("dist")

    for child in results.get("children"):
        hot_list.append(child.get("data").get("title"))

    if after is not None:
        recurse(subreddit=subreddit, hot_list=hot_list,
                after=after, count=count)
    return hot_list
