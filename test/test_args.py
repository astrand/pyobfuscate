#!/usr/bin/env python

import unittest

def function_none():
    pass

def function_args(a, b, c):
    assert a == 1
    assert b == 2
    assert c == 3
    assert "a" in locals()
    assert "b" in locals()
    assert "c" in locals()

def function_default(expected, arg=12):
    assert expected == arg
    assert "expected" in locals()
    assert "arg" in locals()

def function_posargs(*args):
    # FIXME: args could be obfuscated in theory, but the obfuscator is
    #        currently unable.
    #assert "args" not in locals()
    pass

def function_kwargs(**kwargs):
    # FIXME: Dito
    #assert "kwargs" not in locals()
    pass

class FunctionArgumentTest(unittest.TestCase):
    def test_none(self):
        function_none()

    def test_pos(self):
        function_args(1, 2, 3)

    def test_named(self):
        function_args(c=3, b=2, a=1)

    def test_default(self):
        function_default(12)

    def test_default_pos(self):
        function_default(13, 13)

    def test_default_named(self):
        function_default(13, arg=13)

    def test_posargs(self):
        function_posargs()
        function_posargs(1, 2, 3)

    def test_kwargs(self):
        function_kwargs()
        function_kwargs(a=1, b=2, c=3)

class Dummy:
    def method_none(self):
        pass

    def method_args(self, a, b, c):
        assert a == 1
        assert b == 2
        assert c == 3
        assert "a" in locals()
        assert "b" in locals()
        assert "c" in locals()

    def method_default(self, expected, arg=12):
        assert expected == arg
        assert "expected" in locals()
        assert "arg" in locals()

class MethodArgumentTest(unittest.TestCase):
    def test_none(self):
        obj = Dummy()
        obj.method_none()

    def test_pos(self):
        obj = Dummy()
        obj.method_args(1, 2, 3)

    def test_named(self):
        obj = Dummy()
        obj.method_args(c=3, b=2, a=1)

    def test_default(self):
        obj = Dummy()
        obj.method_default(12)

    def test_default_pos(self):
        obj = Dummy()
        obj.method_default(13, 13)

    def test_default_named(self):
        obj = Dummy()
        obj.method_default(13, arg=13)

if "__main__" == __name__:
    unittest.main()
