#!/bin/bash
# Sends a GET request to a URL and displays the status code of the response
curl -sL -o /dev/null -w '%{http_code}' -- "$1"
