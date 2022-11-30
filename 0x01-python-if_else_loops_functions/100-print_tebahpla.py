#!/usr/bin/python3

for letter in range(90, 64, -1):
    if (letter  % 2 == 1):
        char_code = letter
    else:
        char_code = letter + 32
    print("{:c}".format(char_code), end="")
