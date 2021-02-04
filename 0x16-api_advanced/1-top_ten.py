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
    try:
        urlex = 'hot.json?limit=10'
        url = 'https://www.reddit.com/r/{}/{}'.format(subreddit, urlex)
        req = requests.get(url, headers={'User-agent': 'hello-student 0.1'})
        j = req.json()
        data = j.get('data').get('children')
        for i in data:
            print(i.get('data').get('title'))
    except AttributeError:
        print(None)
