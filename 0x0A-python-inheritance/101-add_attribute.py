#!/usr/bin/python3

'''
This module defines a function that adds
a new attribute to an object if it's possible
'''


def add_attribute(obj, key, value):
    '''Adds attribute to the object [obj]'''
    if hasattr(obj, '__dict__'):
        obj.__dict__[key] = value
    else:
        raise TypeError("can't add new attribute")
