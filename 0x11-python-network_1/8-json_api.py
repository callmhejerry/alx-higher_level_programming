#!/usr/bin/python3

'''
A script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
'''


if __name__ == "__main__":
    import requests
    import sys

    url = "http://0.0.0.0:5000/search_user"
    data = {}
    try:
        param = sys.argv[1]
        data = {"q": param}
    except Exception:
        data = {"q": ""}
    try:
        with requests.post(url, data=data) as response:
            json_response = response.json()
            if json_response == {}:
                print("No result")
            else:
                id = json_response.get('id')
                name = json_response.get('name')
                print("[{}] {}".format(id, name))
    except Exception:
        print("Not a valid JSON")
