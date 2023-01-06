#!/usr/bin/python3

'''
A function that prints a square with the character #
@size: the size of the square to print
'''


def print_square(size):
    '''prints a square with the character #'''
    if size is None:
        raise TypeError("size must be an integer")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#"*size)
