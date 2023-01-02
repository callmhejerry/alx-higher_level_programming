#!/usr/bin/python3

'''A Square class'''


class Square:
    '''A Square class with a private attribute size'''
    def __init__(self, size=0):
        '''Constructor of the Square class'''
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        '''An instance method to find the area if the square'''
        return self.__size ** 2
