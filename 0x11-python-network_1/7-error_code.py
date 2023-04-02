#!/usr/bin/python3

'''
A script that takes in a url, sends a request to the url
and displays the body of the response
'''


if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]
    with requests.get(url) as response:
        code = response.status_code
        if code >= 400:
            print("Error code:", code)
        else:
            print(response.text)
