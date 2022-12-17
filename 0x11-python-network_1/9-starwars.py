#!/usr/bin/python3
"""
script takes githut credentials and uses it to display id
"""

from sys import argv
import requests


if __name__ == "__main__":
    URL = 'https://api.github.com/user'
    cred = (argv[1], argv[2])
    r = request.get(URL, auth=cred)
    data = r.jason()
    print(data.get('id'))
