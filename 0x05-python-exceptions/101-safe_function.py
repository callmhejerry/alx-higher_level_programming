#!/usr/bin/python3
from sys import stderr
'''a function that executes a function safely'''


def safe_function(fct, *args):
    try:
        first, second = args
        result = fct(first, second)
        return result
    except Exception as exc:
        stderr.write("Exception: {}\n".format(exc))
        return None
