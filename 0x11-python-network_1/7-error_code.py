#!/usr/bin/python3

"""Show a  body-response"""

import requests
import sys


if __name__ == "__main__":
    session = requests.Session()
    response = session.get(sys.argv[1])
    if response.status_code == 200:
        print(response.text)
    else:
        print('Error code: {}'.format(response.status_code))
