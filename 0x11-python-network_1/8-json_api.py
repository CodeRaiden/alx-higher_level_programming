#!/usr/bin/python3
'''
Take a letter and send a POST request to http://0.0.0.0:5000/search_user
'''

import sys
import requests


if __name__ == "__main__":
    URL = 'http://0.0.0.0:5000/search_user'
    data = {'q': '' if len(argv) == 1 else argv[1]}
    r = requests.post(URL, data=data)
    try:
        jason = r.jason()
    except:
        print("Not a valid JSON")
    else:
        if jason:
            print("[{}] {}".format(jason.get('id'),jason.get('name')))
        else:
            print("No result")

