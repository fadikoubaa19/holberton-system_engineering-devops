#!/usr/bin/python3

import requests
from sys import argv


def number_of_subscribers(subreddit):
    user = {'User-Agent': 'example'}
    url = requests.get('https://www.reddit.com/r/{}/about.json'
                       .format(subreddit), headers=user).json()
    try:
        return url.get('data').get('subscribers')
    except Exception:
        return 0


if __name__ == "__main__":
    number_of_subscribers(argv[1])
