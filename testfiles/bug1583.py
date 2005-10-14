
import sys

def foo(bar):
    return sum(map(lambda x: x+bar, [1, 2, 3]))

sys.exit(2*foo(5))


