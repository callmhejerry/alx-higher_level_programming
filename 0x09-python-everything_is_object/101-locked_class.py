#!/usr/bin/python3

'''A locked class'''


class LockedClass:
    '''A lockedclass class'''
    def __setattr__(self, __name, __value):
        '''sets the correct attribute'''
        if __name != "first_name":
            raise AttributeError("'LockedClass'\
 object has no attribute '{}'".format(__name))
        self.__dict__[__name] = __value

    @property
    def first_name(self):
        return self.first_name
