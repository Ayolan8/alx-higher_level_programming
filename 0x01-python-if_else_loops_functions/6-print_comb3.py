#!/usr/bin/python3
for x in range(0, 89):
    if x % 10 > x // 10:
        print("{:02}".format(x), ", ", sep='', end='')
print(89)
