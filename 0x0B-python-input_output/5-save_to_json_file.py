#!/usr/bin/python3

'''
This Module defines a function that
writes an object to a text file using
JSON representation
'''


import json


def save_to_json_file(my_obj, filename):
    '''save the json representation of [my_obj] to [file name]'''
    with open(filename, "w") as file:
        json.dump(my_obj, file)
