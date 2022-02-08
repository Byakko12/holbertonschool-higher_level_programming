#!/usr/bin/python3
"""class Base"""


import json


class Base:
    """contructor of class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init atributte"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to json string"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save to file"""
        filename = cls.__name__ + ".json"
        result = []
        if list_objs:
            for objs in list_objs:
                dictionary = objs.to_dictionary()
                result.append(dictionary)
        with open(filename, "w", encoding="utf-8") as file:
            file.write(cls.to_json_string(result))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)
