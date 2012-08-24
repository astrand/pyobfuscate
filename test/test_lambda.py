#!/usr/bin/env python

import unittest

__all__ = ["public_global"]

private_global = 1
public_global = 2

def arg_func(arg):
    f = lambda : arg
    return f()

class LambdaTest(unittest.TestCase):
    def test_simple(self):
        f = lambda: True
        self.assertTrue(f())

    def test_arg(self):
        f = lambda b: b
        self.assertTrue(f(True))

    def test_local(self):
        var = 3
        f = lambda : var
        self.assertTrue(f() == 3)

    def test_local_arg(self):
        self.assertTrue(arg_func(4) == 4)

    def test_private_global(self):
        self.assertFalse("private_global" in globals())
        f = lambda : private_global
        self.assertTrue(f() == 1)

    def test_public_global(self):
        self.assertTrue("public_global" in globals())
        f = lambda : public_global
        self.assertTrue(f() == 2)

if "__main__" == __name__:
    unittest.main()
