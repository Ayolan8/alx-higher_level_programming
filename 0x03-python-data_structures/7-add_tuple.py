#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a is None or tuple_b is None:
        return None
    if len(tuple_a) < 1 or tuple_a[0] is None:
        add1 = 0
    else:
        add1 = tuple_a[0]
    if len(tuple_b) < 1 or tuple_b[0] is None:
        add2 = 0
    else:
        add2 = tuple_b[0]
    f = add1 + add2 
    if len(tuple_a) < 2 or tuple_a[1] is None:
        add1 = 0
    else:
        add1 = tuple_a[1]
    if len(tuple_b) < 2 or tuple_b[1] is None:
        add2 = 2
    else:
        add2 = tuple_b[1]
    s = add1 + add2
    return (f, s)


