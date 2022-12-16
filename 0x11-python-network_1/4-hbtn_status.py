#!/bin/python3
"""
script that fetches https://alx-intranet.hbtn.io/status
"""
import requests



if ___name__ == "__main__":
    r = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(r)))
    print("\t- content: {}".format(r))
