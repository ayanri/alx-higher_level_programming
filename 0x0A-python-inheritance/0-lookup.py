#!/usr/bin/python3
"""
Returns the list of available attributes amnd methodds of an object:
"""


def lookup(obj):
    """return list of attributes and methods of 'obj'

    Args:
        obj (Any): object

    Returns:
        list: list of attributes and members
    """
    return dir(obj)
