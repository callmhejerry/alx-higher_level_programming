#!/bin/bash
# A script that takes in a URL, sends a GET request to the url, and displays the body of the response
curl -s -L "$1"
