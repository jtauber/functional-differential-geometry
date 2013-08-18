# this works around a path issue with just calling
# coverage run -m doctest -v <rst-file>

import doctest
import sys

doctest.testfile(sys.argv[1], verbose=True)
