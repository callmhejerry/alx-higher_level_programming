#!/usr/bin/python3

'''
A function that prints My name is <first name> <last name>
@first_name : the first name to be printed
@last_name: the last name to be printed, with a default value of ""
'''


def say_my_name(first_name, last_name=""):
    '''prints My name is <first name> <last name>'''
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))

say_my_name("John", "Smith")
say_my_name("Walter", "White")
say_my_name("Bob")
try:
    say_my_name(12, "White")
except Exception as e:
    print(e)