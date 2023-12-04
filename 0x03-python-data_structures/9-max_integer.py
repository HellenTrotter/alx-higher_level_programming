#!/usr/bin/python3
def max_integer(my_list=[]):
    maximum = None
    if len(my_list) > 0:
        maximum = my_list[0]
        for item in my_list:
            if item > maximum:
                maximum = item
    return maximum
