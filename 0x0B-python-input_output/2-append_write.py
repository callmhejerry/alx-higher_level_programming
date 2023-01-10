#!/usr/bin/python3

'''
This Module defines a function that appends a string
at the end of a text file
'''


def append_write(filename="", text=""):
    '''
    appends a text [text] to a file [filename] and return
    the number of characters written
    '''
    written = 0
    with open(filename, 'a', encoding="utf-8") as file:
        written = file.write(text)
    return written
