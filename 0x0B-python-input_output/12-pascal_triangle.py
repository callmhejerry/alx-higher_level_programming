#!/usr/bin/python3

'''
This module defines a function that computes the
pascal triangle of a number
'''


def fact(n):
    '''return the factorial of n'''
    res = 1
    if n == 0 or n == 1:
        return res
    for i in range(1, n + 1):
        res *= i
    return res


def comb(n, r):
    '''retuns n combination r'''
    denominator = fact(n - r) * fact(r)
    numerator = fact(n)
    result = numerator // denominator
    return result


def pascal_row(n):
    '''computes the pascal row'''
    if n == 0:
        return [1]
    row = []
    for i in range(n + 1):
        res = comb(n, i)
        row.append(res)
    return row


def pascal_triangle(n):
    '''compute the pascal triangle'''
    if n <= 0:
        return []
    pascal_list = []
    for i in range(n):
        row = pascal_row(i)
        pascal_list.append(row)
    return pascal_list
