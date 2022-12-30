#!/usr/bin/python3

'''A function that divides 2 integers and
    prints the result'''


def safe_print_division(a, b):
    result = 0

    try:
        result = a / b
    except Exception:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
