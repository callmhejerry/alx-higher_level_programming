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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        '''Sets the private position variable'''
        if (len(value) != 2 or not isinstance(value, tuple)
                or not isinstance(value[0], int)
                or not isinstance(value[1], int)
                or value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        '''returns the area of the square'''
        return self.__size ** 2

    def my_print(self):
        '''prints the square class using #'''
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" "*self.__position[0], end="")
                print("#"*self.__size)

    def __str__(self):
        '''returns a string format of the sqaure class'''
        my_str = ""
        if self.__size == 0:
            return my_str
        else:
            for i in range(self.__position[1]):
                my_str += '\n'
            for i in range(0, self.__size):
                my_str += " "*self.__position[0]
                my_str += "#"*self.__size
                if i != self.__size - 1:
                    my_str += '\n'
        return my_str
