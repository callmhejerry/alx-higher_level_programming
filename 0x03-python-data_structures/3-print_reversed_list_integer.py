#!/usr/bin/python3

'''A function that prints a all integers of a list
    in reverse order'''


def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    for item in my_list:
        print("{:d}".format(item))
