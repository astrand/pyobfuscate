#!/usr/bin/env python
#
# Execute the file with the same name as myself minus the extension.
# Author: Peter Astrand <astrand@cendio.com>
#
import os, sys
root, ext = os.path.splitext(sys.argv[0])
execfile(root)
