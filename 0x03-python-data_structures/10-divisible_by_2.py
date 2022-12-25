#!/usr/bin/python3

'''A function that finds all multiples of 2 in a list'''


def divisible_by_2(my_list=[]):
    new_list = []

    for item in my_list:
        if item % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
