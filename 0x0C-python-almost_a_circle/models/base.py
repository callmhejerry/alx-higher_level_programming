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
        '''
        returns the Json string representation of
        [list_dictionaries]
        '''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        Saves the json representation of list_objs to a file
        '''
        with open("{}.json".format(cls.__name__), "w") as file:
            list_dicts = list(map(lambda item: item.to_dictionary(), list_objs))
            json_str = cls.to_json_string(list_dicts)
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        '''
        returns the list of the JSON string representation
        of [json_string]
        '''
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''
        returns an instance with all attributes already sets
        '''
        dummy_shape = cls(1, 2, 2, 2)
        dummy_shape.update(**dictionary)
        return dummy_shape

    @classmethod
    def load_from_file(cls):
        '''
        Returns a list of instances
        '''
        with open("{}.json".format(cls.__name__)) as file:
            content = file.read()
            list_dct = cls.from_json_string(content)
            list_instance = list(map(lambda dct: cls.create(**dct), list_dct))
            return list_instance
