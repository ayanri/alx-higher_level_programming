#!/usr/bin/python3
for a in range(9):
    for b in range(10):
        if a < b:
            if ((a*10) + b) != 89:
                print("{}{}".format(a, b), end=", ")
            else:
                print("{}{}".format(a, b))
