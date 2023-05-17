#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    arg_nm = len(argv)
    x = 1
    if arg_nm == 0:
        print("{:d} argument.".format(arg_nm))
    elif arg_nm == 1:
        print("{:d} argument.".format(arg_nm))
        print("{:d}: {:s}".format(x, sys.argv[1]))
    else:
        print("{:d} argument.".format(arg_nm))
        while 1 < arg_nm:
            print("{:d}: {:s}".format(x, sys.argv[x]))
            x += 1
