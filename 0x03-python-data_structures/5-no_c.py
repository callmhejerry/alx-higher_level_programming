#!/usr/bin/python3

'''A function that removes all characters c and C
    from a string'''


def no_c(my_string):
    newstr = ''

    for letter in my_string:
        if letter != 'c' and letter != 'C':
            newstr += letter

    return newstr
