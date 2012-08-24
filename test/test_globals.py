#!/usr/bin/env python

import unittest

# Locally defined global variable should be obfuscated
local_global = 1

# Check that referenced are properly followed
local_reffed_global = 2

def check_func_ref(self):
    var = local_reffed_global
    self.assertFalse("var" in locals())
    self.assertEqual(var, 2)

def check_func_write(val):
    global local_reffed_global
    local_reffed_global = val

# Locally defined globals can be missing on the module scope
# Unfortunately we don't know if this variable is only declared here,
# or if it also comes via a * import. The obfuscator assumes the worst
# and lets it remain in the clear.
def check_func_define(self):
    global hidden_local_global
    hidden_local_global = 3
    self.assertFalse("hidden_local_global" in locals())
    self.assertTrue("hidden_local_global" in globals())

# Multiple global references at once
local_global_a = 4
local_global_b = 5

def check_func_multi_write(a, b):
    global local_global_a, local_global_b
    local_global_a = a
    local_global_b = b

class LocalGlobalTest(unittest.TestCase):
    def test_simple(self):
        self.assertFalse("local_global" in globals())

    def test_reffed(self):
        self.assertFalse("local_reffed_global" in globals())

    def test_func_ref(self):
        check_func_ref(self)

    def check_method_ref(self):
        var = local_reffed_global
        self.assertFalse("var" in locals())
        self.assertEqual(var, 2)

    def test_method_ref(self):
        self.check_method_ref()

    def test_func_write(self):
        check_func_write('x')
        self.assertEqual(local_reffed_global, 'x')
        check_func_write(2)
        self.assertEqual(local_reffed_global, 2)

    def check_method_write(self, val):
        global local_reffed_global
        local_reffed_global = val

    def test_method_write(self):
        self.check_method_write('x')
        self.assertEqual(local_reffed_global, 'x')
        self.check_method_write(2)
        self.assertEqual(local_reffed_global, 2)

    def test_func_define(self):
        check_func_define(self)
        self.assertEqual(hidden_local_global, 3)

    def test_multi(self):
        self.assertFalse("local_global_a" in globals())
        self.assertFalse("local_global_b" in globals())

    def test_func_multi_write(self):
        check_func_multi_write('y', 'z')
        self.assertEqual(local_global_a, 'y')
        self.assertEqual(local_global_b, 'z')
        check_func_multi_write(4, 5)
        self.assertEqual(local_global_a, 4)
        self.assertEqual(local_global_b, 5)

    def check_method_multi_write(self, a, b):
        global local_global_a, local_global_b
        local_global_a = a
        local_global_b = b

    def test_method_multi_write(self):
        self.check_method_multi_write('y', 'z')
        self.assertEqual(local_global_a, 'y')
        self.assertEqual(local_global_b, 'z')
        self.check_method_multi_write(4, 5)
        self.assertEqual(local_global_a, 4)
        self.assertEqual(local_global_b, 5)

# Check that external references do not get obfuscated
from global_lib import *

# Local copies should still get obfuscated though
local_copy = external_global_top

def check_func_external_ref(self):
    var = external_global_ro
    self.assertFalse("var" in locals())
    self.assertEqual(var, "b")

def check_func_external_write(val):
    global external_global_rw
    external_global_rw = val

class ExternalGlobalTest(unittest.TestCase):
    def test_name(self):
        self.assertTrue("external_global_top" in globals())
        self.assertTrue("external_global_ro" in globals())
        self.assertTrue("external_global_rw" in globals())

    def test_copy(self):
        self.assertFalse("local_copy" in globals())

    def test_func_ref(self):
        check_func_external_ref(self)

    def check_method_ref(self):
        var = external_global_ro
        self.assertFalse("var" in locals())
        self.assertEqual(var, "b")

    def test_method_ref(self):
        self.check_method_ref()

    def test_func_write(self):
        check_func_external_write('x')
        self.assertEqual(external_global_rw, 'x')
        check_func_external_write("c")
        self.assertEqual(external_global_rw, "c")

    def check_method_write(self, val):
        global external_global_rw
        external_global_rw = val

    def test_method_write(self):
        self.check_method_write('x')
        self.assertEqual(external_global_rw, 'x')
        self.check_method_write("c")
        self.assertEqual(external_global_rw, "c")

if "__main__" == __name__:
    unittest.main()
