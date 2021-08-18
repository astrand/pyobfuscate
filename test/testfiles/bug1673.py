__all__ = ["gvar", "colliding"]
import sys
gvar = 47
def foo():
    global gvar
    gvar += 2
    colliding = 33
    assert 0 == ("colliding" in locals())
    return gvar
sys.exit(foo())

