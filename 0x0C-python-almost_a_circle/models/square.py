#!/usr/bin/python3
'''
This module defines a Square Class that inherits from
Rectangle class
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''A Square class'''
    def __init__(self, size, x=0, y=0, id=None):
        '''
        creates a Square class

        Args:
            size (int): The size attribute for the new Square object
            x (int): The x coordinate for the new Square object
            y (int): The y coordinate for the new Square object
            id (int): The id of the square
        '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Returns the string representation of the Sqaure'''
        return "[Square] ({:d}) {:d}/{:d} - {:d}"\
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        '''returns the size attribute'''
        return self.width

    @size.setter
    def size(self, value):
        '''sets the width and height attribute'''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''
        Update the instance attribute with the args value

        Args:
            *args (ints): New atrribute value
                - 1st argumment represents id attribute
                - 2nd argument represent width attribute
                - 3rd argument represent height attribute
                - 4th argument represent x attribute
                - 5th argument represent y attribute
            **kwargs (dict): New key/value pairs of attribute
        '''
        dct = {}
        if args is not None and len(args) > 0:
            var = ["id", "size", "x", "y"]
            for i in range(len(args)):
                if i == len(args):
                    break
                dct[var[i]] = args[i]
        else:
            dct = kwargs
        for key, value in dct.items():
            if key == "id" and value is None:
                continue
            setattr(self, key, value)

    def to_dictionary(self):
        '''returns the dictionary representation of the Square'''
        dct = {
          'id': self.id,
          'x': self.x,
          'size': self.size,
          'y': self.y
        }
        return dct
