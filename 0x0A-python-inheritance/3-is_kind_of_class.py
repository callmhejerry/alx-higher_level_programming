#!/usr/bin/python3

'''
This module defines a function that checks if
an object is an instance of a class or a class
that derives from the class
'''


def is_kind_of_class(obj, a_class):
    '''
    returns True if the object [obj] is an instance of,
    or if the object is an instance of a class that inherited
    from , the specified class. Return False otherwise
    '''
    return isinstance(obj, a_class)
