#!/usr/bin/python3
""" This module queries the Reddit API and returns
the number of subscribers (not active users, total subscribers)
for a given subreddit. If an invalid subreddit is given,
the function should return 0
"""

import json
import requests
import sys


def number_of_subscribers(subreddit):
    """ This function returns the number of subscribers
    for a given subreddit. If an invalid subreddit is given,
    the function should return 0
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    data = requests.get(url, headers=headers)
    if data.status_code >= 300:
        return 0

    return (data.json().get('data').get('subscribers'))
