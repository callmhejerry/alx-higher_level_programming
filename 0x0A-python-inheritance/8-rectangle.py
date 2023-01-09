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
        try:
            super().integer_validator("width", width)
            super().integer_validator("height", height)
        except Exception:
            raise
        self.__width = width
        self.__height = height
