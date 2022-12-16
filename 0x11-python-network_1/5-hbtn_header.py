#!/usr/bin/python3
"""
script that takes in a url to send a request to the url
and display the values of the variable X-Request-Id
"""
import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get(argv[1])
    print(r.header.get('X-Request-Id'))
