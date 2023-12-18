#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    p_integers = 0
    i = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            p_integers += 1
        except(TypeError, ValueError):
            continue

    print()
    return p_integers
