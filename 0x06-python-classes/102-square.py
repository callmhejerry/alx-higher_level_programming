#!/usr/bin/python3


'''A square class '''


class Square:
    '''A square class with privarte instance variable size'''
    def __init__(self, size=0):
        self.size = size

    def area(self):
        '''returns the area os the square instance'''
        return self.__size ** 2

    @property
    def size(self):
        '''retrieves the private size variable'''
        return self.__size
    
    @size.setter
    def size(self, value):
        '''sets the private size variable'''
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        else:
            raise TypeError("size must be an integer")

    def __eq__(self, other):
        '''implement the equality
            comparison sign to compare two
            instances of this class'''
        return self.__size == other.size

    def __ne__(self, other):
        '''implement the "not equal" comparison
            operator for two instances of the
            square class'''

        return self.__size != other.size

    def __lt__(self, other):
        '''returns true if first instance is less than
            the second instance of the square class'''
        return self.__size < other.size

    def __gt__(self, other):
        '''returns true if first instance is greater than
            the second instance of the square class'''
        return self.__size > other.size

    def __le__(self, other):
        '''returns true if first instance is less than
            or equal to the second instance of the
             square class'''
        return self.__size <= other.size
    
    def __ge__(self, other):
        '''returns true if first instance is greater than
            or equal to the second instance of the
             square class'''
        return self.__size >= other.size

    def __hash__(self):
        '''returns the hash value of the object'''
        return hash(self.__size)
