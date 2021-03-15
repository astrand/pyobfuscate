import sys

import tobeimported_noall

if (tobeimported_noall.one() + tobeimported_noall.two()) != 3:
    sys.exit(-1)

sys.exit(1)