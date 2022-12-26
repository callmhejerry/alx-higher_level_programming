#!/usr/bin/python3

'''A fucntion that replaces all occurences
    of an element by another in a new list'''


def search_replace(my_list, search, replace):
    new_list = []
    for item in my_list:
        if item is search:
            new_list.append(replace)
        else:
            new_list.append(item)
    return new_list
