#!/usr/bin/env python3

import unittest

# Note: read-only non-local bindings are tested in test_locals.py

def check_func(self):
    def nested(self, val):
        nonlocal var
        var = val
    var = 1
    self.assertFalse("var" in locals())
    self.assertFalse("nested" in locals())
    nested(self, 'x')
    self.assertEqual(var, 'x')
    nested(self, 2)
    self.assertEqual(var, 2)

def check_func_double(self):
    def nested_a(self, val):
        var2 = 2
        def nested_b(self, val1, val2):
            nonlocal var1
            nonlocal var2
            var1 = val1
            var2 = val2
        self.assertFalse("var2" in locals())
        self.assertFalse("nested_b" in locals())
        nested_b(self, 'x', 'y')
        self.assertEqual(var1, 'x')
        self.assertEqual(var2, 'y')
        nested_b(self, 3, 4)
        self.assertEqual(var1, 3)
        self.assertEqual(var2, 4)
        nested_b(self, val, val)
    var1 = 1
    self.assertFalse("var1" in locals())
    self.assertFalse("nested_a" in locals())
    nested_a(self, 'z')
    self.assertEqual(var1, 'z')
    nested_a(self, 5)
    self.assertEqual(var1, 5)

def check_func_multi(self):
    def nested(self, val1, val2):
        nonlocal var1, var2
        var1 = val1
        var2 = val2
    var1 = 1
    var2 = 2
    self.assertFalse("var1" in locals())
    self.assertFalse("var2" in locals())
    self.assertFalse("nested" in locals())
    nested(self, 'x', 'y')
    self.assertEqual(var1, 'x')
    self.assertEqual(var2, 'y')
    nested(self, 3, 4)
    self.assertEqual(var1, 3)
    self.assertEqual(var2, 4)

class NonlocalTest(unittest.TestCase):
    def test_func(self):
        check_func(self)

    def test_method(self):
        def nested(self, val):
            nonlocal var
            var = val
        var = 1
        self.assertFalse("var" in locals())
        self.assertFalse("nested" in locals())
        nested(self, 'x')
        self.assertEqual(var, 'x')
        nested(self, 2)
        self.assertEqual(var, 2)

    def test_func_double(self):
        check_func_double(self)

    def test_method_double(self):
        def nested_a(self, val):
            var2 = 2
            def nested_b(self, val1, val2):
                nonlocal var1
                nonlocal var2
                var1 = val1
                var2 = val2
            self.assertFalse("var2" in locals())
            self.assertFalse("nested_b" in locals())
            nested_b(self, 'x', 'y')
            self.assertEqual(var1, 'x')
            self.assertEqual(var2, 'y')
            nested_b(self, 3, 4)
            self.assertEqual(var1, 3)
            self.assertEqual(var2, 4)
            nested_b(self, val, val)
        var1 = 1
        self.assertFalse("var1" in locals())
        self.assertFalse("nested_a" in locals())
        nested_a(self, 'z')
        self.assertEqual(var1, 'z')
        nested_a(self, 5)
        self.assertEqual(var1, 5)

    def test_func_multi(self):
        check_func_multi(self)

    def test_method_multi(self):
        def nested(self, val1, val2):
            nonlocal var1, var2
            var1 = val1
            var2 = val2
        var1 = 1
        var2 = 2
        self.assertFalse("var1" in locals())
        self.assertFalse("var2" in locals())
        self.assertFalse("nested" in locals())
        nested(self, 'x', 'y')
        self.assertEqual(var1, 'x')
        self.assertEqual(var2, 'y')
        nested(self, 3, 4)
        self.assertEqual(var1, 3)
        self.assertEqual(var2, 4)

if "__main__" == __name__:
    unittest.main()
