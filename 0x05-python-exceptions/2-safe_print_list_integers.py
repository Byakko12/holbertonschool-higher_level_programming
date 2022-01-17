#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    for data in my_list:
        try:
            if data <= x:
                print("{:d}".format(data), end="")
        except ValueError:
            pass
        except TypeError:
            pass
        counter += 1
    print()
    return counter
