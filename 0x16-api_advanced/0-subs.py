#!/usr/bin/python3
"""
subs counting
"""
import requests
from sys import argv
"""
function number_of_subscirbers
"""


def number_of_subscribers(subreddit):
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    try:
        req = requests.get(url, headers={'User-agent': 'fedi'})
        subs = req.json()
        return subs.get('data').get('subscribers')
    except AttributeError:
        return 0
