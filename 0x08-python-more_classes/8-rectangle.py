#!/usr/bin/python3

'''a class Rectangle that defines a rectangle by: (based on 7-rectangle.py)'''


class Rectangle:
    '''A Rectangle class'''
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        '''initializes the Rectangle class'''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        '''returns the string representation of
            the Rectangle class with "#"'''
        my_str = ""
        if self.height == 0 or self.width == 0:
            return my_str
        for i in range(self.height):
            my_str += str(self.print_symbol) * self.width
            if i != self.height - 1:
                my_str += '\n'
        return my_str

    def __repr__(self):
        '''returns a formal representation of the
         Rectangle class'''
        return 'Rectangle({}, {})'.format(self.width, self.height)

    def __del__(self):
        '''deletes an instance Rectangle'''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
