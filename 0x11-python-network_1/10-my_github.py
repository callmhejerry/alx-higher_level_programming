#!/usr/bin/python3

'''
A script that takes your GITHUB credentials and uses the
Github api to display your id
'''


if __name__ == "__main__":
    import requests
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": password,
        "X-GitHub-Api-Version": '2022-11-28'
    }
    auth = (username, password)
    with requests.get(url, headers=headers, auth=auth) as response:
        json_response = response.json()
        json_id = json_response.get('id')
        print(json_id)
