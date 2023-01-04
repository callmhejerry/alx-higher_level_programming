#!/usr/bin/python3

'''
A function that divides all elements of a matrix
matrix - the matrix to be divided
div -  the divisor
'''


def matrix_divided(matrix, div):
    '''
    divides the matrix by div
    '''
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")

    try:
        size_of_row = len(matrix[0])
    except Exception:
        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")

    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
        if len(row) != size_of_row:
            raise TypeError("Each row of the matrix must have the same size")
        for cell in row:
            if type(cell) not in [int, float]:
                raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")

    result = []
    for row in range(len(matrix)):
        temp = []
        for col in range(len(matrix[row])):
            cell = matrix[row][col]
            res = round(cell / div, 2)
            temp.append(res)
        result.append(temp)

    return result
