#!/usr/bin/env python3
#
# Execute the file with the same name as myself minus the extension.
# Author: Peter Astrand <astrand@cendio.se>
#
import os, sys
root, ext = os.path.splitext(sys.argv[0])
exec(compile(open(root, "rb").read(), root, 'exec'))
