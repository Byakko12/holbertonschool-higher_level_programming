#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    counter = 0
    for data in my_list:
        try:
            if data <= x:
                print("{}".format(data), end="")
                counter += 1
        except:
            break
    print()
    return counter
