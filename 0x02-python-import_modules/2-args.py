#!/usr/bin/python3
import sys

if __name__ == '__main__':
    argv = sys.argv
    argc = len(argv) - 1
    i = 1

    if argc == 0:
        print("{} arguments.".format(argc))
    elif argc > i:
        print("{} arguments:".format(argc))
        while i <= argc:
            print("{}: {}".format(i, argv[i]))
            i += 1
    else:
        print("{} argument:".format(argc))
        print("{}: {}".format(i, argv[i]))
