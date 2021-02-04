#!/usr/bin/python3
"""
subs counting
"""
import requests
from sys import argv
"""
function number_of_subscirbers
"""


def recurse(subreddit, hot_list=[]):
    try:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
        req = requests.get(url, headers={'User-Agent': 'f'}), para = {'l': 100}
        data = req.json()
        hot_list.extend(data['data']['children'])
        page = data['data']['after']
        if data['data']['after'] is None:
            return
    except KeyError:
        return None
    recursive(subreddit, hot_list, page)
    return hot_list


def recursive(subreddit, hot_list=[], page=""):
    """handles the other entries"""
    if page is None:
        return
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    req = requests.get(url, headers={'User-Agent': 'f'}),
    para = {'after': page, 'l': 100}
    data = req.json()
    hot_list.extend(data['data']['children'])
    return recursive(subreddit, hot_list, data['data']['after'])
