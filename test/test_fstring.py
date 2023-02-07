#!/usr/bin/env python3

import sys
import unittest

globalval = 999

class C:
    foo = 42
    pass
c = C()

multiline = f"""
param1={globalval}
param2={c.foo}
"""

class FStringTest(unittest.TestCase):
    def test_strings(self):
        value = 17
        self.assertEqual(f"{value*value}", "289")
        self.assertEqual(f"{value!s}", "17")
        self.assertEqual(f"{value:4}", "  17")
        self.assertEqual(f"{globalval}dollars", "999dollars")
        self.assertTrue(f"{sys.version}".startswith("3."))
        self.assertEqual(multiline, """
param1=999
param2=42
""")

        self.assertEqual(f"a {value} "
                         f"b {globalval} ", "a 17 b 999 ")
        self.assertEqual(f"{{ {value} }}", "{ 17 }")
        

if "__main__" == __name__:
    unittest.main()
