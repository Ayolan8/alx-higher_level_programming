#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argCount = len(argv) - 1
    if argCount == 0:
        print("{:d} arguments".format(argCount))
    else:
        if argCount == 1:
            print("{:d} argument:".format(argCount))
        elif argCount > 1:
            print("{} arguments:".format(argCount))
        for num, item in enumerate(argv[1:], start=1):
            print("{} {}".format(num, item))
