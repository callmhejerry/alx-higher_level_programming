#!/usr/bin/python3

'''
This module defines a class that inherits from
the built-in list class
'''


class MyList(list):
    '''MyList class inherits from the List built-in class'''
    def __init__(self):
        '''intializes the MyList class'''
        super().__init__()

    def print_sorted(self):
        print(sorted(self))

    def append(self, __object: int) -> None:
        if type(__object) is int:
            super().append(__object)
