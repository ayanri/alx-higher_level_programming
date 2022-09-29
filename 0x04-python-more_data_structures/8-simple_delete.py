#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for a in a_dictionary:
        if a == key:
            del a_dictionary[key]
            break
    return a_dictionary
