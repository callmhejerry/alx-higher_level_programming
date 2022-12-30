#!/usr/bin/python3

'''A function that prints an integer'''


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except TypeError as type:
        print("Exception: {}".format(type))
        return False
