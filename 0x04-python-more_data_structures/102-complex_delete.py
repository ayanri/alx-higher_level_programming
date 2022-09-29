#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    tmp = a_dictionary.copy()
    for a, x in tmp.items():
        if value == x:
            a_dictionary.pop(a)
    return a_dictionary
