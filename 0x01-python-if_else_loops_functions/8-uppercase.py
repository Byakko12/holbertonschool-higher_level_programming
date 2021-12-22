#!/usr/bin/python3
def uppercase(str):
    for i in str:
        characters = ord(i)
        if characters >= 97 and characters <= 122:
            characters = chr(characters - 32)
        else:
            characters = i
        print("{}".format(characters), end="")
    print("")
