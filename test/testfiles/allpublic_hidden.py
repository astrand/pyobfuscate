import sys

import tobeimported_noall

try:
    tobeimported_noall._hidden()
except AttributeError:
    sys.exit(1)

sys.exit(-1)