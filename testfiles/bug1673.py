__all__ = ["gvar"]
import sys
gvar = 47
def foo():
    global gvar
    gvar += 2
    return gvar
sys.exit(foo())

