#!/usr/bin/python3

'''This module defines a BaseGeometry class'''


class BaseGeometry():
    '''A BaseGeometry class'''
    def area(self):
        '''raise an exception'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(name) is str:
            if type(value) is not int:
                raise TypeError("{} must be an integer".format(name))
            if value <= 0:
                raise ValueError("{} must be greater than 0".format(name))
