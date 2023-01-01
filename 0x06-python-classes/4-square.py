#!/usr/bin/python3


'''A square class '''


class Square:
    def __init__(self, size=0):
        self.size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            self.size = value
        else:
            raise TypeError("size must be an integer")
