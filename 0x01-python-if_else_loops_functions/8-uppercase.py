#!/usr/bin/python3

def uppercase(str):
    for letter in str:
        if (ord(letter) >= 97 and ord(letter) <= 122):
            print("{:c}".format(ord(letter) - 32), end="")
        else:
            print("{:c}".format(ord(letter)), end="")
    else:
        print("")
