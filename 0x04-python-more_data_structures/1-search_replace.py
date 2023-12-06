#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list_copy = []
    for i in my_list:
        if i == search:
            list_copy.append(replace)
        else:
            list_copy.append(i)
    return list_copy
