#!/usr/bin/python3

'''
This Module defines a base [base] class 
'''


import json


class Base():
    '''A Base class'''
    __nb_objects = 0

    def __init__(self, id=None) -> None:
        '''creates the Base class instance'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects +=1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        with open("{}.json".format(cls.__name__), "w") as file:
            list_dicts = list(map(lambda item: item.to_dictionary(), list_objs))
            json_str = Base.to_json_string(list_dicts)
            file.write(json_str)
