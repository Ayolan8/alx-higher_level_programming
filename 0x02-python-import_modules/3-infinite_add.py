#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    arg_nm = len(argv) - 1
    if arg_nm == 0:
        print("{}".format(arg_nm))
    else:
        res = []
        for x in range(1, arg_nm + 1):
            res.append(int(argv[x]))
        print("{}".format(sum(res)))
