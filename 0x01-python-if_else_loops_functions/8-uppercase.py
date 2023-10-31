#!/usr/bin/python3
def uppercase(str):
    for cap in str:
        char = cap
        if ord(cap) >= ord('a') and ord(cap) <= ord('z'):
            char = chr(ord(letter) - 32)
        print("{}".format(char), end='')
    print("")
