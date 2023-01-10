#!/usr/bin/python3

'''
This Module defines a function that reads
a text file and prints it to standard output
'''
import sys

def read_file(filename=""):
    '''reads the contents in a file [filename] and prints in stdout'''
    with open(filename) as file:
        for line in file:
            sys.stdout.write(line)


read_file("my_file_0.txt")