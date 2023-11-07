#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argCount = len(argv)
    if argCount <= 0:
        print("0 arguments.")
    else:
        if argCount == 2:
            print(argCount - 1, "argument:")
        else:
            print(argCount - 1, "arguments:")
        for num, value in enumerate(argv[1:], start=1):
            print("{} {}".format(num, value))
