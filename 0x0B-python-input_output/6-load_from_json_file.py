#!/usr/bin/python3


'''
This Module defines a function that creates
an object from a "JSON file"
'''


import json

def load_from_json_file(filename):
    '''returns an object loaded from a JSON file'''
    with open(filename, "r") as file:
        return json.load(file)
