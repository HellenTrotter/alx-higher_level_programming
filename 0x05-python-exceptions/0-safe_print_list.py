#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    n = 0
    printed = 0
    for n in range(0, x):

        try:
            print("{}".format(my_list[n]), end="")
            printed += 1

        except:
            continue

    print()
    return printed
