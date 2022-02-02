#!/usr/bin/python3
"""read_file"""


def read_file(filename=""):
    with open(filename, encoding="utf-8") as textfile:
        for line in textfile:
            print(line, end="")
