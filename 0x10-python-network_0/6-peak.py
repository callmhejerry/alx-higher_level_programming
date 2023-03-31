#!/usr/bin/python3

'''
A script that finds the peak in a list
'''


def find_peak(list_of_integers):
    '''return the peak in the list'''

    if list_of_integers is None or len(list_of_integers) == 0:
        return None
    
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    
    mid = len(list_of_integers) // 2
    left_peak = find_peak(list_of_integers[:mid])
    right_peak = find_peak(list_of_integers[mid:])
    
    if left_peak > right_peak:
        return left_peak
    return right_peak
    