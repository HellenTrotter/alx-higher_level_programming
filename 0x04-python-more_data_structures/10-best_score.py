#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    biggest_int = 0
    best_value = ""
    for key, value in a_dictionary.items():
        if value > biggest_int:
            biggest_int = value
            best_value = key
    return best_value
