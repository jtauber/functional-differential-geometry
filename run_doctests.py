# this works around a path issue with just calling
# coverage run -m doctest -v <rst-file>

import doctest
import sys

fails = 0

for filename in [
    "tuples.rst",
    "functions.rst",
    "symbolic.rst",
    "simplification.rst",
    "differentiation.rst",
    "symbolic_tuples.rst",
]:
    result = doctest.testfile(filename)
    fails += result.failed

if fails:
    sys.exit(1)
