#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    kkeys = list(sorted((a_dictionary.keys())))
    for x in kkeys:
        print("{}: {}".format(x, a_dictionary[x]))
