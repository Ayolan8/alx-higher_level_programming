#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return (0)
    av = 0
    size = 0
    for x in my_list:
        av += (x[0] * x[1])
        size += (x[1])
    return (av / size)
