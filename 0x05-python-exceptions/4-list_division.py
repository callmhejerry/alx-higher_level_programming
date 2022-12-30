#!/usr/bin/python3

'''A function that divides element by element 2 lists'''


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    result = 0

    for idx in range(0, list_length):
        try:
            result = my_list_1[idx] / my_list_2[idx]
        except IndexError:
            print("out of range")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        finally:
            new_list.append(result)
    return new_list
