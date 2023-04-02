#!/usr/bin/python3

'''
A script that takes in a url and an email address, sends a POST
request to the passed url with the email as a parameter, and
finally displays the body of the response
'''


if __name__ == "__main__":
    import requests
    import sys

    email = sys.argv[2]
    url = sys.argv[1]
    data = {"email": email}
    with requests.post(url, data=data) as response:
        print(response.text)
