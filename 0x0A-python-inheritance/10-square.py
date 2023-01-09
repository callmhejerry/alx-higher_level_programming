#!/usr/bin/python3

'''
This module defines a Square class that inherits
from a Rectangle class
'''


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    '''A Square class'''
    def __init__(self, size):
        '''creates a Square object'''
        Rectangle.integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size

    def area(self):
        '''return the area of the square shape'''
        return self.__size ** 2
