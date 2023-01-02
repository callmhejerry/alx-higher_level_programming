#!/usr/bin/python3


'''A Square class'''


class Square:
    '''A square class with a private instacnce
        variable size'''
    def __init__(self, size=0):
        '''initializes the square class with a size variable'''
        self.size = size

    @property
    def size(self):
        '''a getter fucntion to retrieve the private size variable'''
        return self.__size

    @size.setter
    def size(self, value):
        '''sets the privated size variable with value'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        '''returns the area of the square'''
        return self.__size ** 2

    def my_print(self):
        '''prints the square class using #'''
        if self.__size == 0:
            print("")
        for i in range(0, self.__size):
            print("#"*self.__size)
