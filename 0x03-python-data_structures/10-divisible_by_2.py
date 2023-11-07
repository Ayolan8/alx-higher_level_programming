#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    list_div = []
    for x in my_list:
        if x < 0: 
            x = -1
        if (1 % 2) ==0:
            list_div.append(True)
        else:
            list_div.appemd(False)
    return list_div
