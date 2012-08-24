
import sys

def sort(x, y):
    return cmp(x,y)

def main():
    l = [120,300,42]
    l.sort(lambda x, y: sort(x, y))
    return l[0]


if "__main__" == __name__:
    sys.exit(main())
