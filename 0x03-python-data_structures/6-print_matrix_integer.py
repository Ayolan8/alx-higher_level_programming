#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    for rw in matrix:
        if rw is not None and len(rw) > 0 and rw[0] is not None:
            print("{:d}".format(rw[0]), end="")
            if len(rw) > 1:
                for cl in rw[1:]:
                    print("{:d}".format(cl), end="")
        print()
