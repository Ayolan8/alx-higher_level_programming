#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import hidden_4.pyc
    for x in dir(hidden_4):
        if x[:2] != "__":
            print(x)
