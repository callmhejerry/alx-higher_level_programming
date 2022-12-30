#!/usr/bin/python3

'''A function that prints the first x elements of a list
    and only integers'''


def safe_print_list_integers(my_list=[], x=0):
    num_printed = 0

    for idx in range(0, x):
        try:
            if isinstance(my_list[idx], int):
                print("{:d}".format(my_list[idx]), end="")
            else:
                continue
            num_printed += 1
        except IndexError:
            raise
    print("")
    return num_printed
