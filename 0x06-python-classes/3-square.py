#!/usr/bin/python3
""" a class Square that defines a square"""


class Square:
    """A class defined for square generation

    Args:
    size: length of one size of the square

    Attributes:
    __size: length of one side of the square

    Raises:
    TypeError: if size is not an int
    ValueError: if size is less than 0

    """

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """returns the area"""

        return self.__size**2
