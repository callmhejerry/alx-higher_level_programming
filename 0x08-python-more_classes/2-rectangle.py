#!/usr/bin/python3

'''a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)'''


class Rectangle:
    '''A Rectangle class'''
    def __init__(self, width=0, height=0):
        '''initializes the Rectangle class'''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''retrieves the private width variable'''
        return self.__width

    @width.setter
    def width(self, value):
        '''sets the private width variable'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''retrieves the private height variable'''
        return self.__height

    @height.setter
    def height(self, value):
        '''sets the private height variable'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''returns the area of the Rectangle object'''
        return self.height * self.width

    def perimeter(self):
        '''returns rthe perimeter of the Rectangle object'''
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.width + self.height)
