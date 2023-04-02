#!/usr/bin/python3

'''
A script that fetches the git commits from a
a github api
'''


if __name__ == "__main__":
    import sys
    import requests

    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    headers = {
        'X-GitHub-Api-Version': '2022-11-28',
        "accept": "application/vnd.github+json"
        }
    params = {
        "per_page": 10,
    }

    with requests.get(url, headers=headers, params=params) as response:
        if response.status_code == 200:
            json_reponse = response.json()
            for item in json_reponse:
                sha = item.get('sha')
                name = item.get('commit').get('author').get('name')
                print("{}: {}".format(sha, name))
