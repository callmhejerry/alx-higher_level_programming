#!/bin/bash
# A script that takes in a url as an arguement, sends a get request to the url and displays the body of the response
curl -s -H "X-School-User-Id:98" "$1"
