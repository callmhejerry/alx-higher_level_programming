#!/usr/bin/python3
'''
A script that takes in a URL, sends a request to the url
and displays the value of the variable x-request-Id
'''


if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    with requests.get(url) as response:
        print(response.headers.get('X-Request-Id'))
