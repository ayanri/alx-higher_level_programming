#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_directory = {}
    for a in a_dictionary:
        new_directory[a] = a_dictionary[a] * 2
    return new_directory
