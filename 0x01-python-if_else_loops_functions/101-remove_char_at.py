#!/usr/bin/python3

def remove_char_at(str, n):
    copy = ""
    if (n < 0):
        return str
    for index in range(len(str)):
        if (index != n):
            copy += str[index]
    return copy
