#!/usr/bin/python3

'''
A script that takes in a url,sends a request to the url and
displays the body of the response
'''
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            body = body.decode("UTF-8")
            print(body)
    except urllib.error.HTTPError as error:
        print("Error code:", error.code)
