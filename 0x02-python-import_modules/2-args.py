#!/usr/bin/python3
import sys

if __name__ == "__main__":

    counter = 0
    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print("{:d} argument:".format(len(sys.argv) - 1))
        print("{:d}: {}".format(len(sys.argv) - 1, sys.argv[1]))
    else:
        print("{:d} argument:".format(len(sys.argv) - 1))
        for i in sys.argv:
            if counter >= 1:
                print("{:d}: {}".format(counter, i))
            counter += 1
