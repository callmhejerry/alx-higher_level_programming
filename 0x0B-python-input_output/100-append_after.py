#!/usr/bin/python3

'''
This Module defines a function that inserts a
line of text to a file, after each line containing
a specific string
'''


def append_after(filename="", search_string="", new_string=""):
    '''
    inserts a string [new_string] in file [filename]
    after each line containing a string [search_string]
    '''
    lines = ""
    with open(filename, encoding="utf-8") as file:
        for line in file:
            lines += line
            if search_string in line:
                lines += new_string
    with open(filename, "w", encoding="utf-8") as file:
        file.write(lines)
