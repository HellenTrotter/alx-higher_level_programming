#!/usr/bin/python3
"""a class MyList that inherits from list"""


class MyList(list):
    """inherits from list"""
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))

