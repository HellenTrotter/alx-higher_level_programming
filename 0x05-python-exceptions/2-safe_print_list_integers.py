#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    p_integers = 0
    try:
        for i in range(x):
            value = my_list[i]
            if type(value) == int:
                print("{:d}".format(value), end="")
                p_integers += 1
    except(TypeError, ValueError):
        pass

    print()
    return p_integers
