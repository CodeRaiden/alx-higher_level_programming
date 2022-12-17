#!/usr/bin/python3
'''
Send an email to a URL using a POST request and display the response body
'''

import sys
import requests


if __name__ = "__main__":
    email = {'email': sys.argv[1]}
    URL = sys.argv[2]
    r = requests.get(URL, data=email)
    print(r.text)
