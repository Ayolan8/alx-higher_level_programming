#!/usr/bin/python3
def magic_calculation(a, b):
    if a < b:
        c = add(a, b)
        for x in range(a, b): 
            c = add(c, x)
        return c
    else:
        return sub(a, b)
    return
