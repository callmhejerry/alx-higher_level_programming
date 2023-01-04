#!/usr/bin/python3

'''
A function that adds two numbers
a - the first argument
b - the second argument with a default value of 98
'''


def add_integer(a, b=98):
    '''
    returns the addition of a and b
    '''
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
