#
# A comment at top.
#

import sys

a = 12

b = 16

c = 14

def test():
    return a+b+c

if "__main__" == __name__:
    sys.exit(test())
