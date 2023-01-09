#!/usr/bin/python3

'''
This module defines a function that checks if an
object is an instance of a class that inherits from
a class directly or indirectly
'''


def inherits_from(obj, a_class):
    '''
    Returns True if the obj is an instance of a class that
    inherits directly or indeirectly from [a_class], returns
    False otherwise
    '''
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
