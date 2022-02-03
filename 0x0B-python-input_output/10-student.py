#!/usr/bin/python3
"""class Student"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None:
            list = {}
            for i in attrs:
                if i in self.__dict__:
                    list[i] = self.__dict__[i]
            return list
        return self.__dict__
