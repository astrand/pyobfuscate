#!/usr/bin/env python3
# -*- coding: ISO-8859-15 -*-
import unittest

class SourceCodeEncodingDeclarationTest(unittest.TestCase):
    def test_default_encoding(self):
        symbol = "€"
        codepoint = "\u20ac"
        self.assertEqual(symbol, codepoint)

if "__main__" == __name__:
    unittest.main()