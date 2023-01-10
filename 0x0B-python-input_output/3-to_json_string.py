#!/usr/bin/python3

'''
This module defines a function that returns the
JSON representation of an object
'''


import json

def to_json_string(my_obj):
    '''returns the JSON representation of my_obj'''
    return json.dumps(my_obj)
