#!/usr/bin/python3
'''
List 10 commits (newest to oldest) of the repo "rails" by the user "rails"
'''

from sys import argv
import requests



if __name__ == '__main__':
    URL = 'https://api.github.com/repos/{owner}/{repo}commits'
    r = requests.get(URL.format(repo = argv[1], owner = argv[2]))
    for item in response.jason()[:10]:
        print("{}: {}".format(item['sha'], item['commit']['author']['name']))
