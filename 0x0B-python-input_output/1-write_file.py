#!/usr/bin/python3
"""write_file"""


def write_file(filename="", text=""):
    """file function"""
    with open(filename, 'w', encoding="utf-8") as file:
        return(file.write(text))
