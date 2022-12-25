#!/usr/bin/python3

'''A function that replaces an element in a list
    at a specific position without modifying the original list'''


def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    if idx < 0 or idx >= len(my_list):
        return new_list
    new_list[idx] = element
    return new_list
