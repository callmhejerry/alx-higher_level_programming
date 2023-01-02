#!/usr/bin/python3


'''A Square class'''


class Square:
    '''A square class with a private instacnce
        variable size and position'''
    def __init__(self, size=0, position=(0, 0)):
        '''initializes the square class with a size variable
            and a positon variable'''
        self.position = position
        self.size = size

    @property
    def size(self):
        '''a getter fucntion to retrieve the private size variable'''
        return self.__size

    @property
    def position(self):
        '''retrieves the private position variable '''
        return self.__position

    @size.setter
    def size(self, value):
        '''sets the privated size variable with value'''
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        else:
            raise TypeError("size must be an integer")

    @position.setter
    def position(self, value):
        '''Sets the private position variable'''
        if len(value) == 2:
            first, second = value
            if first >= 0 and second >= 0:
                self.__position = value
            else:
                raise TypeError("position must be a tuple \
                    of 2 positive integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        '''returns the area of the square'''
        return self.__size ** 2

    def my_print(self):
        '''prints the square class using #'''
        if self.__size == 0:
            print("")
        for i in range(0, self.__size):
            print(" "*self.__position[0], end="")
            print("#"*self.__size)
