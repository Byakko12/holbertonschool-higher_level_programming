#!/usr/bin/python3
"""method"""


def append_write(filename="", text=""):
    """file function"""
    with open(filename, 'a', encoding="utf-8") as file:
        return(file.write(text))
