#!/usr/bin/python3
'''
Send a request to a URL and display the body of the response
'''

from sys import argv
import requests



if __name__ == "__main__":

    if len(sys.argv) != 2:
        print('Usage: ', __file__, 'URL', file=sys.stderr)
        sys.exit(1)

    r = requests.get(arg[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
