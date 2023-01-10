#!/usr/bin/python3

'''
This Module defines a function that writes
a string to a text file and returns the number
of characters written
'''


def write_file(filename="", text=""):
    '''
    Writes a text [text] to a file [filenamme] and return the
    number of characters written
    '''
    written = 0
    with open(filename, "w", encoding="utf-8") as file:
        written = file.write(text)
    return written
