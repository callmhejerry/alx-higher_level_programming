#!/usr/bin/python3

def uppercase(str):
    for letter in str:
        if (ord(letter) >= 97 and ord(letter) <= 122):
            char_code = ord(letter) - 32
        else:
            char_code = ord(letter)
        print("{:c}".format(char_code), end="")
    else:
        print("")
