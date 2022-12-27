#!/usr/bin/python3


'''A function that returns a key with the biggest integer value'''


def best_score(a_dictionary):
    if len(a_dictionary) is 0 or a_dictionary is None:
        return None
    scores = a_dictionary.values()
    biggest_value = scores[0]

    for score in scores:
        if score >= biggest_value:
            biggest_value = score
    return biggest_value
    