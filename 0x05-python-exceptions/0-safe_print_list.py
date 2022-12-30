#!/usr/bin/python3

'''A function that prints x elements of a list'''


def safe_print_list(my_list=[], x=0):
    num_printed = 0

    try:
        for idx in range(0, x):
            print("{}".format(my_list[idx]), end="")
            num_printed += 1
        print("")
    except Exception:
        print("")
    return num_printed
