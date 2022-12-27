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
    tmp = roman_string[0]

    for letter in roman_string:
        if letter in roman:
            if roman[letter] > roman[tmp]:
                num -= roman[tmp]
                num += (roman[letter] - roman[tmp])
                tmp = letter
            else:
                num += roman[letter]
                tmp = letter
    return num
