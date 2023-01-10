#!/usr/bin/python3

'''
This Module defines a Student class
'''


class Student():
    '''Student class'''
    def __init__(self, first_name, last_name, age):
        '''creates the student object'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''Return the dictionary representation of student object'''
        return self.__dict__
