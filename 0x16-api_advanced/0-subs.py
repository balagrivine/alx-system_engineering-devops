#!/usr/bin/python3


"""function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.
"""

import requests

def number_of_subscribers(subreddit):
    """queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit"""

    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {'User-Agent': 'My user Agent 1.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data =  response.json().get('data', {})
        sub_count = data.get('subscribers', 0)

        return sub_count
    else:
        return 0
