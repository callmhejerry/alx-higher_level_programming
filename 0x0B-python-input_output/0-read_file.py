#!/usr/bin/python3

'''
This Module defines a function that reads
a text file and prints it to standard output
'''


def read_file(filename=""):
    '''reads the contents in a file [filename] and prints in stdout'''
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content, end="")
