#!/usr/bin/python3

'''
This module defines a Rectangle class that inherits from
the base class
'''


from base import Base


class Rectangle(Base):
    '''A Rectangle class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''creates the Rectangle class instance'''
        Base.__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
