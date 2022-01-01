#!/usr/bin/python3
import sys

if __name__ == "__main__":

    counter = 0
    sum = 0
    if len(sys.argv) == 1:
        print("0")
    elif len(sys.argv) == 2:
        print("{}".format(sys.argv[1]))
    else:
        for i in sys.argv:
            if counter >= 1:
                sum += int(i)
            counter += 1
        print("{}".format(sum))
