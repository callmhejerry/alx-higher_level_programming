#!/usr/bin/python3


'''A function that returns a key with the biggest integer value'''


def best_score(a_dictionary):
    if len(a_dictionary) is 0 or a_dictionary is None:
        return None
    keys = a_dictionary.key()
    biggest_value = keys[0]

    for score in keys:
        if a_dictionary[biggest_value] >= a_dictionary[biggest_value]:
            biggest_value = score
    return biggest_value
