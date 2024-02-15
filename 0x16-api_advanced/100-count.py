#!/usr/bin/python3
"""
This function that queries the Reddit API recursively.
"""
import requests


def count_words(subreddit, word_list, after='', word_count={}):
    """Queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit
    """

    if not word_count:
        for word in word_list:
            if word.lower() not in word_count:
                word_count[word.lower()] = 0

    if after is None:
        word_dict = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for word in word_dict:
            if word[1]:
                print('{}: {}'.format(word[0], word[1]))
        return None

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    header = {"User-Agent": "AppleWebKit:0x16.api.advanced:v1.0.0 \
                       (by /u/JazzlikeFig4018)"}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=header, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    try:
        hot_post = response.json()['data']['children']
        after = response.json()['data']['after']
        for post in hot_post:
            title = post['data']['title']
            lower = [word.lower() for word in title.split(' ')]

            for word in word_count.keys():
                word_count[word] += lower.count(word)

    except Exception:
        return None

    count_words(subreddit, word_list, after, word_count)
