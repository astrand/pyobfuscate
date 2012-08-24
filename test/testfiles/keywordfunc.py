
import sys

SOMETHING=21

def foo(bar=SOMETHING):
    return bar

def gazonk(startval=2):
    return startval + foo()

if "__main__" == __name__:
    sys.exit(gazonk(startval=21))




