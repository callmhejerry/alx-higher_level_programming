#!/usr/bin/python3

'''
This module defines MyInt class that inherits from Int
'''


class MyInt(int):
    '''MyInt class'''
    def __init__(self, num) -> None:
        '''Creates a MyInt object'''
        int.__init__(self)

    def __eq__(self, __x: object) -> bool:
        '''implements the equality sign'''
        return not super().__eq__(__x)

    def __ne__(self, __x: object) -> bool:
        '''implements the inequality sign'''
        return not super().__ne__(__x)
