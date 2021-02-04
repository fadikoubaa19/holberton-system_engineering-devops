#!/usr/bin/python3
"""
subs counting
"""
import requests
from sys import argv
"""
function number_of_subscirbers
"""


def top_ten(subreddit):
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    try:
        req = requests.get(url, headers={'User-agent': 'fedi'})
        for post in url.get('data').get('children'):
            print(post.get('data').get('title'))
    except Exception:
        print(None)


if __name__ == "__main__":
    top_ten(argv[1])
