
__all__ = ["ClassWithKeywords"]

class ClassWithKeywords:
    def __init__(self, kwarg = 3):
        self.kwarg = kwarg

    def fortytwo(self, arg=6):
        return self.kwarg + arg
        
