#!/usr/bin/python3

'''
A script that takes in a url, sends a request to the url
and displays the value of the X-REQUEST-ID variable found in
the header of the response.
'''


if __name__ == "__main__":
    import sys
    import urllib.request

    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        value = response.getheader('X-Request-Id')
        print(value)
