#!/usr/bin/python3

'''
This module defines MyInt class that inherits from Int
'''


class MyInt(int):
    '''MyInt class'''
    def __init__(self) -> None:
        '''Creates a MyInt object'''
        super().__init__()

    def __eq__(self, __x: object) -> bool:
        '''implements the equality sign'''
        return not super().__eq__(__x)

    def __ne__(self, __x: object) -> bool:
        '''implements the inequality sign'''
        return not super().__ne__(__x)
