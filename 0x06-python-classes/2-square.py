#!/usr/bin/python3
"""defines a class square, implements its value, type checks its attributes"""


class Square:
    """Square Implementation"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
