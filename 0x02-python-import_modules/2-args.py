#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    k = len(sys.argv) - 1

    if k == 0:
        print("{} arguments.".format(k))
    elif k == 1:
        print("{} argument:".format(k))
    else:
        print("{} arguments:".format(k))
    for i in range(k):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
