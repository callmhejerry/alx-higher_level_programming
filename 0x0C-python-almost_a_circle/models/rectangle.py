#!/usr/bin/python3

'''
This module defines a Rectangle class that inherits from
the base class
'''
from models.base import Base


class Rectangle(Base):
    '''A Rectangle class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        """

        Args:
            width (int): The width of the Rectangle
            height (int): The height of the new Rectangle
            x (int): the x coordinates of the new Rectangle
            y (int): the y coordinate of the new Rectangle
        Raises:
            TypeError: If either of the width or the height is not an integer
            ValueError: If either of the width or the height <= 0
            TypeError: If either of the x or y is not an integer
            ValueError: If either of the x or y is < 0
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''returns the width property'''
        return self.__width

    @property
    def height(self):
        '''returns the height property'''
        return self.__height

    @property
    def x(self):
        '''returns the x property'''
        return self.__x

    @property
    def y(self):
        '''returns the y property'''
        return self.__y

    @width.setter
    def width(self, value):
        '''sets the private width property'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        '''sets the private height property'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        '''sets the private x property'''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        '''sets the private y property'''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''returns the area of the Rectangle'''
        return self.height * self.width

    def display(self):
        '''prints the Rectangle instance with the #'''
        for y in range(self.y):
            print()
        for h in range(self.height):
            if self.x > 0:
                print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self) -> str:
        '''returns the string representation of the Rectangle class'''
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"\
            .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwagrs):
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
            var = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                if i == len(var):
                    break
                dct[var[i]] = args[i]
        else:
            dct = kwagrs
        for key, value in dct.items():
            if key == "id" and value is None:
                continue
            setattr(self, key, value)

    def to_dictionary(self):
        '''Returns the dictionary representation of Rectangle class'''
        dct = {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width
        }
        return dct
