#!/usr/bin/python3
for num01 in range(10):
    for num02 in range(10):
        if num02 > num01 and num01 != 8:
            print("{}{}".format(num01, num02), end=", ")
        elif num01 == 8 and num02 == 9:
            print("{}{}".format(num01, num02))
            break
