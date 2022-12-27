#!/usr/bin/python3


'''A function that returns a key with the biggest integer value'''


def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    keys = list(a_dictionary.keys())
    biggest_value = keys[0]

    for score in keys:
        if a_dictionary[score] >= a_dictionary[biggest_value]:
            biggest_value = score
    return biggest_value
