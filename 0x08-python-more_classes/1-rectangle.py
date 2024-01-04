#!/usr/bin/python3
""" class Rectangle that defines a rectangle by: (based on 0-rectangle.py) """


class Rectangle:
    """ class Rectangle """

    def __init__(self, width=0, height=0):
        """ initialisation of default width and height """

        self.height = height
        self.width = width

    @property
    def height(self):
        """ height """

        return self.__height

    @property
    def width(self):
        """ width """

        return self.__width

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return self.__height * 2 + self.__width * 2
