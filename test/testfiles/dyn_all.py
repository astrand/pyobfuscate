foo = ["aaa"]
__all__ = ["bbb"] + foo

def bbb():
    return 40

def aaa():
    return 2
