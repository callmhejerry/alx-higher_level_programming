#!/usr/bin/python3

'''A function that prints a all integers of a list
    in reverse order'''


def print_reversed_list_integers(my_list = []):
    new_list = my_list.copy().reverse()

    for item in new_list:
        print("{:d}".format(item))
