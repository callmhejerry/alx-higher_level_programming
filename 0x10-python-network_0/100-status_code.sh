#!/bin/bash
# a script that sends a request to a url passed as an argument, and displays only the status code
curl -s -o /dev/null -w '%{http_code}' "$1"
