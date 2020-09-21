#!/usr/bin/env python3

import unittest

# Check that multi line literals don't get destroyed.
#
# Bug 1: Line starting with a string was assumed to be a doc string
#
dictionary = {
    'key1': (12, 'foobar', None,
             "another string", 44,
             "foo",
             None),
    'key2': (12, 'foobar', None,
             "another string", 44,
             "foo",
             None)
    }

class LiteralTest(unittest.TestCase):
    def test_dictionary(self):
        self.assertTrue("key1" in list(dictionary.keys()))
        self.assertTrue("key2" in list(dictionary.keys()))
        self.assertEqual(dictionary["key1"][5], "foo")
        self.assertEqual(dictionary["key2"][5], "foo")

if "__main__" == __name__:
    unittest.main()
