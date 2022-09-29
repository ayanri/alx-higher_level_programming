#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    level = 0
    for a in a_dictionary:
        if a_dictionary[a] is None:
            return None
        if level == 0:
            high = a_dictionary[a]
        if a_dictionary[a] > high:
            high = a_dictionary[a]
        level += 1

    for x in a_dictionary:
        if a_dictionary[x] == high:
            return x
