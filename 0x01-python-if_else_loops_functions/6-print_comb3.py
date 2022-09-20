#!/usr/bin/pyhton3
for a in range(9):
    for b in range(10):
        if a < b:
            if ((i*10) + b) != 89:
                print("{}{}".format(a, b), end=", ")
            else:
                print("{}{}".format(a, b))
