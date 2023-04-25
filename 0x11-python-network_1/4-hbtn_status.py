#!/usr/bin/python3
'''
A script that fetches content from a url
'''


if __name__ == "__main__":
    import requests

    url = "https://alx-intranet.hbtn.io/status"
    with requests.get(url) as response:
        print("Body response:")
        print("\t- type: {}".format(type(response.text)))
        print("\t- content: {}".format(response.text))
