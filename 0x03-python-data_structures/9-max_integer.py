#!/usr/bin/python3
'''A fucntion that finds the biggest
    integer in a list'''


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max_num = 0
    for num in my_list:
        if num >= max_num:
            max_num = num
    return max_num
