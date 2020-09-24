#!/usr/bin/env python3

import unittest

__all__ = ["GlobalClass"]

class LocalClass:
	def method_a():
		pass

class GlobalClass:
	def method_b():
		pass

class OuterNestedClass:
	class InnerNestedClass:
		pass

def nested_function(test):
	class InnerNestedClass:
		pass
	test.assertFalse("InnerNestedClass" in locals())

# This crashed the obfuscator at one point
class EmptyAncestors():
	pass

class LocalAncestor(LocalClass):
	pass

class GlocalAncestor(GlobalClass):
	pass

class MixedAncestors(LocalClass, GlobalClass):
	pass

class ClassTest(unittest.TestCase):
	def test_local(self):
		self.assertFalse("LocalClass" in globals())

	def test_local_method(self):
		obj = LocalClass()
		# Method names should not be obfuscated as we don't
		# know what the object is until runtime
		self.assertTrue(hasattr(obj, "method_a"))

	def test_global(self):
		self.assertTrue("GlobalClass" in globals())

	def test_global_method(self):
		obj = GlobalClass()
		# See test_local_method()
		self.assertTrue(hasattr(obj, "method_b"))

	def test_nested_class(self):
		self.assertFalse("OuterNestedClass" in globals())
		self.assertTrue(hasattr(OuterNestedClass, "InnerNestedClass"))

	def test_nested_function(self):
		nested_function(self)

	def test_local_ancestor(self):
		self.assertFalse("LocalClass" in globals())
		self.assertFalse("LocalAncestor" in globals())
		self.assertTrue(issubclass(LocalAncestor, LocalClass))

	def test_global_ancestor(self):
		self.assertTrue("GlobalClass" in globals())
		self.assertFalse("GlocalAncestor" in globals())
		self.assertTrue(issubclass(GlocalAncestor, GlobalClass))

	def test_mixed_ancestors(self):
		self.assertFalse("LocalClass" in globals())
		self.assertTrue("GlobalClass" in globals())
		self.assertFalse("MixedAncestors" in globals())
		self.assertTrue(issubclass(MixedAncestors, LocalClass))
		self.assertTrue(issubclass(MixedAncestors, GlobalClass))

if "__main__" == __name__:
    unittest.main()
