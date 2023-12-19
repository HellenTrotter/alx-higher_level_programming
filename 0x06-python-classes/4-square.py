#!/usr/bin/python3
"""a class Square that defines a square"""


class Square:
    """A class defined for square generation

    Args:
    value: size of square
    """

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """Returns: private size"""

        return self.__size

    @size.setter
    def size(self, value):
        """Sets value into int size

        Args:
        value: size of the square
        """

        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """Returns area"""

        return self.__size**2
