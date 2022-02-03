#!/usr/bin/python3
"""save_to_json_file method"""
import json


def save_to_json_file(my_obj, filename):
    """function"""
    with open(filename, "w", encoding="utf-8") as f:
        return(json.dump(my_obj, f))
