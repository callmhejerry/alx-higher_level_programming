'''
This module defines a function that returns a list of
available attributes and methods of an object
'''


def lookup(obj):
    '''
    Returns a list of the attributes and methods defined
    in the object obj
    '''
    return dir(obj);
