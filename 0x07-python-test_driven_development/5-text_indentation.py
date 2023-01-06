#!/usr/bin/python3

'''
A function that prints a text with 2 new lines after each
of these characters: . ? :
@text: the text to print
'''


def text_indentation(text):
    '''Prints the indentation of text'''
    if type(text) is not str:
        raise TypeError("text must be a string")
    my_str = ""
    allow_space = False

    for s in text:
        if allow_space or s != " ":
            my_str += s
            allow_space = True
            if s in ".?:":
                print(my_str)
                print()
                allow_space = False
                my_str = ""
    if my_str != "":
        print(my_str, end="")
