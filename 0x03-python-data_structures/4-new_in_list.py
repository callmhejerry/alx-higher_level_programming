#!/usr/bin/python3

'''A function that replaces an element in a list
    at a specific position without modifying the original list'''

def new_in_list(my_list, idx, element):
    if idx < 0 and idx >= len(my_list):
        return None
    
    new_list = my_list.copy()
    new_list[idx] = element
    return new_list
