#!/usr/bin/env python

import unittest

__all__ = ["public_variable"]

def function_write(test):
	just_write = 1
	test.assertFalse("just_write" in locals())

def function_read_write(test):
	read_write = 2
	if read_write:
		pass
	test.assertFalse("read_write" in locals())

def function_public(test):
	# A different variable mentioned in __all__ shouldn't
	# prevent obfuscation
	public_variable = 3
	test.assertFalse("public_variable" in locals())

def function_nested(test):
	# Nested function definitions makes the scope handling really
	# confusing
	def nested(test):
		test.assertTrue(var == 12)
	var = 12
	test.assertFalse("var" in locals())
	test.assertFalse("nested" in locals())
	nested(test)

def function_double_nested(test):
	def nested_a(test):
		def nested_b(test):
			test.assertTrue(var == 666)
		test.assertFalse("nested_b" in locals())
	var = 666
	test.assertFalse("var" in locals())
	test.assertFalse("nested_a" in locals())
	nested_a(test)

class FunctionTest(unittest.TestCase):
	def test_just_write(self):
		function_write(self)

	def test_read_write(self):
		function_read_write(self)

	def test_public(self):
		function_public(self)

	def test_nested(self):
		function_nested(self)

	def test_double_nested(self):
		function_double_nested(self)

class Dummy:
	def method_write(self, test):
		just_write = 1
		test.assertFalse("just_write" in locals())

	def method_read_write(self, test):
		read_write = 2
		if read_write:
			pass
		test.assertFalse("read_write" in locals())

	def method_public(self, test):
		# A different variable mentioned in __all__ shouldn't
		# prevent obfuscation
		public_variable = 3
		test.assertFalse("public_variable" in locals())

class MethodTest(unittest.TestCase):
	def test_just_write(self):
		obj = Dummy()
		obj.method_write(self)

	def test_read_write(self):
		obj = Dummy()
		obj.method_read_write(self)

	def test_public(self):
		obj = Dummy()
		obj.method_public(self)

if "__main__" == __name__:
    unittest.main()
