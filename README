
pyobfuscate - Python source code obfuscator
===========================================

pyobfuscate is a source code obfuscator: It makes Python source code
hard to read for humans, while still being executable for the Python
interpreter. 


Why obfuscate?
--------------

Obfuscation makes little sense for Open Source
(http://www.opensource.org/) programs, but vendors developing
commercial applications are usually not happy with shipping the
original source code to customers. 

Several obfuscators for other languages, like Java, already
exists. With Python, the problem is even more severe than with Java,
because Python bytecode is not compatible between different Python
versions. Also, bytecode is very easy to "decompile" to source code by
using "decompyle": http://www.crazy-compilers.com/decompyle/.

If shipping original source code is the only option for distributing
Python applications, then many vendors might choose another
programming language instead. 


What does pyobfuscate do?
-------------------------

pyobfuscate transforms the source code in several ways. Some of these
transformations are reversible (can be "un-obfuscated"); some are
not. Here's a list of what pyobfuscate currently does:

* Removes comments and docstrings (not reversible)

* Changes indentation (reversible)

* Adds whitespace between tokens (somewhat reversible)

* Renames functions, classes and variables (not reversible)

* Inserts bogus lines instead of blank lines. 


Limitations
-----------

pyobfuscate operates on one single source file at a time. It does not
obfuscate the interface between several files. 

pyobfuscate cannot obfuscate methods, class variables or other
attributes, currently. See the TODO for more information.


