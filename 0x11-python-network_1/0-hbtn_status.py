#!/usr/bin/python3
'''
Makes a request and prints information about the body of the response
'''
import urllib.request



if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response
        body = response.read()
    print("Body response:$")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode(encoding="utf -8")))
