#!/usr/bin/python3


'''A function thart returns the weighted average of all
    integers tuple'''


def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    weight_mul = 0
    weighted_sum = 0

    for tuple in my_list:
        score, weight = tuple
        weight_mul += score * weight
        weighted_sum += weight
    weighted_average = weight_mul / weighted_sum
    return weighted_average
