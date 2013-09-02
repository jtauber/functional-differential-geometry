"""
see ``differentiation.rst`` for an explanation.
"""

import numbers

from simplification import simplify
from symbolic import *


def D(expr, wrt):
    if isinstance(expr, numbers.Number):
        return 0
    elif isinstance(expr, Num):
        return 0
    elif isinstance(expr, Sym):
        if expr == wrt:
            return 1
        else:
            return 0
    elif isinstance(expr, Add):
        return simplify(D(expr.arg1, wrt) + D(expr.arg2, wrt))
    elif isinstance(expr, Mul):
        return simplify(D(expr.arg1, wrt) * expr.arg2 + D(expr.arg2, wrt) * expr.arg1)
    elif isinstance(expr, Pow):
        if expr.arg1 == wrt and isinstance(expr.arg2, Num):
            return simplify(expr.arg2 * (expr.arg1 ** (expr.arg2 - 1)))
        else:
            raise NotImplementedError("haven't implemented differentiation of powers in the general case")
    else:
        raise TypeError("can't handle {}".format(type(expr)))