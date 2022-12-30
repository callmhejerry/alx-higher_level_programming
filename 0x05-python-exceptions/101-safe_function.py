#!/usr/bin/python3

'''a function that executes a function safely'''
from sys import stderr

def safe_function(fct, *args):
    try:
        first, second = args
        return fct(first, second)
    except Exception as exc:
        stderr.write("Exception: {}\n".format(exc))
        return None
