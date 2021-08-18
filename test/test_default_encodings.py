#!/usr/bin/env python3
# No encoding given here, will use Python 3 default (utf-8)
import unittest

class SourceCodeDefaultEncodingTest(unittest.TestCase):
    def test_default_encoding(self):
        symbol = "€"
        codepoint = "\u20ac"
        self.assertEqual(symbol, codepoint)

if "__main__" == __name__:
    unittest.main()