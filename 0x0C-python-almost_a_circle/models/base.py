#!/usr/bin/python3

'''
This Module defines a base [base] class 
'''


class Base():
    '''A Base class'''
    __nb_objects = 0

    def __init__(self, id=None) -> None:
        '''creates the Base class instance'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects +=1
            self.id = Base.__nb_objects
