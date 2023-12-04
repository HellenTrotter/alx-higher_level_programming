#!/usr/bin/python3
def no_c(my_string):
    new = ''
    for chars in range(len(my_string)):
        if (my_string[chars] != 'c' and my_string[chars] != 'C'):
            new += my_string[chars]
    return new
