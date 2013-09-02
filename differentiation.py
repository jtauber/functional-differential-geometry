"""
see ``differentiation.rst`` for an explanation.
"""

import numbers

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
        return D(expr.arg1, wrt) + D(expr.arg2, wrt)
    elif isinstance(expr, Mul):
        # technically, the else case coveres this case too but this will give
        # a better answer for this common case before we've implemented
        # simplication
        if isinstance(expr.arg1, Num) and expr.arg2 == wrt:
            return expr.arg1
        else:
            return D(expr.arg1, wrt) * expr.arg2 + D(expr.arg2, wrt) * expr.arg1
    elif isinstance(expr, Pow):
        if expr.arg1 == wrt and isinstance(expr.arg2, Num):
            return expr.arg2 * (expr.arg1 ** (expr.arg2 - 1))
        else:
            raise NotImplemented("haven't implemented differentiation of powers in the general case")
    else:
        raise TypeError("can't handle {}".format(type(expr)))