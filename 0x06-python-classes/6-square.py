#!/usr/bin/python3


'''A Square class'''


class Square:
    def __init__(self, size=0, position=(0,0)):
        self.position = position
        self.size = size

    @property
    def size(self):
        return self.__size
    
    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        else:
            raise TypeError("size must be an integer")

    @position.setter
    def position(self, value):
        if len(value) == 2:
            first, second = value
            if first >= 0 and second >= 0:
                self.__position = value
            else:
                raise TypeError("position must be a tuple of 2 positive integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print("")
        for i in range(0, self.__size):
            print(" "*self.__position[0], end="")
            print("#"*self.__size)
