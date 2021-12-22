#!/usr/bin/python3
def remove_char_at(str, n):
    str2 = ""
    if n > len(str) or n < 0:
        return str
    for i in str:
        if i != str[n]:
            str2 += i
    return str2
