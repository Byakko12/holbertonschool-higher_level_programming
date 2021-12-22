#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number %= -10
        number *= -1
        print("{:d}".format(number), end="")
    else:
        number %= 10
        print("{:d}".format(number), end="")
    return number
