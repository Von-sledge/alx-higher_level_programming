#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL
# Displays the body of the response
curl -s -L -X GET "$1"
