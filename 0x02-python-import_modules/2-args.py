#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argCount = len(argv)
    if argCount == 0:
        print("0 argumentis.")
    else:
        if argCount == 1:
            print("1 argument:")
        else:
            print("{} arguments:".format(argCount))
        for num, value in enumerate(argv[1:], 1):
            print("{} {}".format(num, value))
