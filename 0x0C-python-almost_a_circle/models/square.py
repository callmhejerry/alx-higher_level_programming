#!/usr/bin/python3

'''
This module defines a Square Class that inherits from
Rectangle class
'''


from rectangle import Rectangle


class Square(Rectangle):
    '''A Square class'''
    def __init__(self, size, x=0, y=0, id=None):
        '''creates a Square class'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Returns the string representation of the Sqaure'''
        return "[Square] ({:d}) {:d}/{:d} - {:d}"\
            .format(self.id, self.x, self.y, self.width)
