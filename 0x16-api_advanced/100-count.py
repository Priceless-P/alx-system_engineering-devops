#!/usr/bin/python3
"""
Recurse it!
This function queries a list of all
hot posts on a given Reddit subreddit.
"""
import requests


def count_words(subreddit, word_list, instances={}, after="", count=0):
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
    try:
        results = res.json()
        if res.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return

    results = res.json().get("data")
    after = results.get("after")
    count += results.get("dist")

    for child in results.get("children"):
        titles = child.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in titles:
                times = len([t for t in titles if t == word.lower()])
                if instances.get(word) is None:
                    instances[word] = times
                else:
                    instances[word] += times

    if after is None:
        if len(instances) == 0:
            print("")
            return
        instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
        for k, v in instances:
            print("{}: {}".format(k, v))
    else:
        count_words(subreddit, word_list, instances, after, count)
