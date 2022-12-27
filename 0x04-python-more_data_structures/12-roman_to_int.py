#!/usr/bin/python3

'''A fucniton that converts a roman numeral to an integer'''


def roman_to_int(roman_string):
    if roman_string is None or not(isinstance(roman_string, str)):
        return 0
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    num = 0
    for letter in roman_string.upper():
        if letter in roman:
            num += roman[letter]
    return num
