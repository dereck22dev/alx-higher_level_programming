#!/usr/bin/python3

"""Featch user 10 commits"""

import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])
    session = requests.Session()
    response = session.get(url)
    json_res = response.json()
    i = 0
    for commit in json_res:
        if i < 10:
            print('{}: {}'.format(commit.get('sha'),
                                  commit.get('commit').get('author')
                                  .get('name')))
        i += 1
