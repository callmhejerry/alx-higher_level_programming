#!/usr/bin/python3

'''A function that prints a matrix of integers'''



def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for idx in range(0, len(row)):
            print("{:d}".format(row[idx]), end='')
            if idx != len(row) - 1:
                print(" ", end='')
        print()
