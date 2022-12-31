#!/usr/bin/python3

def magic_calculation(a, b):
    result = 0

    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            else:
                b = a ** b
                i = b / i
                i = result + i
                result = i
        except Exception:
            a = a + b
            result = a
            break
    return result
