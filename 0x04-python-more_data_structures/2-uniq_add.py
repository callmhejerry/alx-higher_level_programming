#!/usr/bin/python3

'''A fucntion that adds all unique integers
    in a list(only once for each integer'''


def uniq_add(my_list=[]):
    result = 0
    for item in set(my_list):
        result += item
    return result
