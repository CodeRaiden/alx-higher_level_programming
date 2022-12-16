#!/usr/bin/python3
"""
Script that fetches https://intranet.hbtn.io/status
"""

from urllib.request import urlopen

URL = 'https://intranet.hbtn.io/status'




if __name__ == '__main__':

    with urlopen(URL) as r:
        body = r.read()
        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)
        print("\t- utf8 content:", body.decode())
