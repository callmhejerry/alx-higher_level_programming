#!/usr/bin/python3

'''
This module defines a class Rectangle that
inherits from BaseGeometry
'''


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    '''A Rectangle class'''
    def __init__(self, width, height) -> None:
        '''creates a Rectangle object'''
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''Returns the area of the Rectangle object'''
        return self.__height * self.__width

    def __str__(self) -> str:
        return "[{}] {}/{}".format(type(self).__name__, self.__width, self.__height)
