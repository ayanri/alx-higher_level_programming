#!/usr/bin/python3
"""defines a class Square, implements value, typechecks for its attributes"""


class Square:
    """square implementation"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise TypeError('size ust be >= 0')
        self.__size = size

    def area(self):
        """calculates the square area"""
        return (self.size ** 2)

    def my_print(self):
        """prints a square with the corresponding size"""
        if (self.__size == 0):
            print('')
        else:
            for x in range(self.position[1]):
                print('')

            for x in range(self.size):
                print(' ' * self.position[0] + '#' * self.size)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if type(position) != tuple or len(position) != 2 or \
            not all(isinstance(z, int) for z in position) or \
                not all(z >= 0 for z in position):
            raise TypeError('position must be a tuple of 2 positive integers')

            self.__position = position
