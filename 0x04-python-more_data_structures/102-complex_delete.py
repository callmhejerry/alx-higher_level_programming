#!/usr/bin/python3

'''A fucntion that deletes keys with a specific value
    in a dictionary'''


def complex_delete(a_dictionary, value):
    items = list(a_dictionary.items())

    for item in items:
        key, val = item
        if val == value:
            del a_dictionary[key]
    return a_dictionary
