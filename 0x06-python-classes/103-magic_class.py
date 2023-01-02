#!/usr/bin/python3


'''A Magic class'''


import math


class MagicClass:
    def __init__(self, radius):
        if type(radius) is not int:
            if type(radius) is not float:
                raise TypeError('radius must be a number')
            else:
                self.radius = radius    
        else:
            self.radius = radius

    def area(self):
        return math.pi  * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius