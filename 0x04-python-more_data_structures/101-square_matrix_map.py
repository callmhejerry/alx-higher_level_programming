#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    squares = map(lambda row: list(map(lambda x:  x ** 2, row)),matrix)
    return list(squares)