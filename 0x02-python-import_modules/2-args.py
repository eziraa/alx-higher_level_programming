#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 0
    arglen = len(sys.argv) - 1
    if arglen == 1:
        print("1 argument", end="")
    elif arglen != 1:
        print("{} arguments".format(arglen), end="")
    if arglen == 0:
        print(".")
    else:
        print(":")
    if(len(sys.argv) > 1):
        for arg in sys.argv:
            if i > 0:
                print("{:d}: {}".format(i, arg))
            i += 1
