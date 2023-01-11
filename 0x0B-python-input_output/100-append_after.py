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
    lines = []
    with open(filename) as file:
        lines = file.readlines()
    with open(filename, "w") as file:
        for line_num in range(len(lines)):
            if lines[line_num].find(search_string) >= 0:
                if line_num == len(lines) - 1:
                    lines.append(new_string)
                else:
                    lines.insert(line_num + 1, new_string)
        file.writelines(lines)
