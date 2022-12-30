#!/usr/bin/python3
import sys

'''A function that prints an integer'''


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as value:
        print("Exception: {}".format(value))
        return False
