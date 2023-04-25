#!/bin/bash
# A bash script that takes in a url and displays all the HTTP methods the sever will accept
curl -s -I "$1" | grep Allow | cut -d " " -f2-
