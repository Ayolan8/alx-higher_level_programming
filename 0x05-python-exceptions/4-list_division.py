#!/usr/bin/python3
def list_division(my_list1, my_list2, list_length):
    my_new_list = []
    for x in range(0, list_length):
        try:
            division = my_list1[x] / my_list2[x]
        except TypeError:
            print("wrong type")
            division = 0
        except ZeroDivisionError:
            print("division by 0")
            division = 0
        except IndexError:
            print("out of range")
            division = 0
        finally:
            my_new_list.append(division)
    return (my_new_list)
