import sys
import functools

def smallest(x, y):
    return min(x, y)

def main():
    l = [120, 300, 42]
    return functools.reduce(lambda x, y: smallest(x, y), l)


if "__main__" == __name__:
    sys.exit(main())
