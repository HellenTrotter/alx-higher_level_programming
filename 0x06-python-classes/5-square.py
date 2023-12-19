#!/usr/bin/python3
"""a class Square that defines a square"""


class Square:
    """class square that defines a square

    Args:
    value: size of the square
    """

    def __init__(self, size=0):

        self.size = size

    @property
    def size(self):
        """Returns: private size"""

        return self.__size

    @size.setter
    def size(self, value):
        """Sets value into size

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
        """Returns: area"""

        return self.__size**2

    def my_print(self):
        """prints the square with the character #"""

        if self.__size != 0:
            for i in range(self.__size):
                for k in range(self.__size):
                    print('#', end='')
                print()
        else:
            print()
