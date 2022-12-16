#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and displays the body of the response
"""
import urllib.request
import urllib.parse
from urllib.error import URLError, HTTPError
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as resp
        print(resp.read().decode(encoding="utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
