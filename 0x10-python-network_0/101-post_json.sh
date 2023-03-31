#!/bin/bash
# A script that sends a JSON POST request to a url
curl -s -X POST -H 'Content-Type: application/json' --data-binary @"$2" "$1"
