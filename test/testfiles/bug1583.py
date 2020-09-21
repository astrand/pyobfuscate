
import sys

def foo(bar):
    return sum([x+bar for x in [1, 2, 3]])

sys.exit(2*foo(5))


