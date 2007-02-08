#!/usr/bin/env python

DESCRIPTION = """\
Python source code obfuscator
"""

from distutils.core import setup

setup (name = "pyobfuscate",
       version = "0.3",
       license = "GPL",
       description = "pyobfuscate",
       long_description = DESCRIPTION,
       author = "Peter Astrand",
       author_email = "astrand@cendio.se",
       url = "http://www.lysator.liu.se/~astrand/projects/pyobfuscate/",
       data_files=[('/usr/bin', ['pyobfuscate'])]
       )
