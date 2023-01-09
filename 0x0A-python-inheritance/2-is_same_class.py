#!/usr/bin/python3

'''
This module defines a function that checks if an
object is an instance of another class
'''


def is_same_class(obj, a_class):
    '''
    this function returns True if the object [obj] is
    exactly an instance of the specified class. Return
    False othewise
    '''
    return isinstance(obj, a_class)
