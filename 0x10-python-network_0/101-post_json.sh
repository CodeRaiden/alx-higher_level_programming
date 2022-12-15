#!/bin/bash
# Sends a POST request to a URL using JSON data and displays the response body
curl -sL -H 'Content-Type: application/json' -d "@$2" -- "$1"
