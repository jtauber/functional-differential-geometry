# this works around a path issue with just calling
# coverage run -m doctest -v <rst-file>

import doctest

for filename in [
    "tuples.rst",
    "functions.rst",
    "symbolic.rst",
    "simplification.rst",
    "differentiation.rst",
    "symbolic_tuples.rst",
]:
    doctest.testfile(filename, verbose=True)
