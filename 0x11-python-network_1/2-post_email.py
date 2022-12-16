#!/usr/bin/python3
'''
Send an email to a URL using a POST request and display the response body
'''

from sys import argv
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = argv[1]
    data = {'email': argv[2]}
    email = urllib.parse.urlencode(data)
    email = email.encode('ascii')
    req = urllib.request.Request(url, email)
    with urllib.request.urlopen(req) as resp:
        body = resp.read()
    print(body.decode(encoding="utf-8"))
