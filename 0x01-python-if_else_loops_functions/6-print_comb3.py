#!/usr/bin/python3

for first in range(9):
    for second in range(first + 1, 10):
        if (first != 8):
            print("{:d}{:d}".format(first, second), end=", ")
        else:
            print("{:d}{:d}".format(first, second))
