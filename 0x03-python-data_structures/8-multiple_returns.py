#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return (len(sentence), None)
    for a in sentence:
        return (len(sentence), a)
