#!/usr/bin/python3

'''
A script that takes in a url and an email, sends a POST request
to the passed URL with the email as a parameter, and displays
the body of the response
'''


if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.parse

    url = sys.argv[1]
    email = sys.argv[2]
    data = {
        "email": email
    }
    data = urllib.parse.urlencode(data)
    data = data.encode('ascii')
    with urllib.request.urlopen(url, data) as response:
        body = response.read()
        body = body.decode('utf-8')
        print(body)
