"""
see ``differentiation.rst`` for an explanation.
"""

import numbers

from simplification import simplify
from symbolic import Num, Sym, Add, Mul, Pow


def D(expr, wrt):  # pylint: disable=C0103
    """
    Differentiate ``expr`` with respect to ``wrt``.
    """
    if isinstance(expr, numbers.Number):
        derivative = 0
    elif isinstance(expr, Num):
        derivative = 0
    elif isinstance(expr, Sym):
        if expr == wrt:
            derivative = 1
        else:
            derivative = 0
    elif isinstance(expr, Add):
        derivative = simplify(D(expr.arg1, wrt) + D(expr.arg2, wrt))
    elif isinstance(expr, Mul):
        derivative = simplify(
            D(expr.arg1, wrt) * expr.arg2 +
            D(expr.arg2, wrt) * expr.arg1
        )
    elif isinstance(expr, Pow):
        if expr.arg1 == wrt and isinstance(expr.arg2, Num):
            derivative = simplify(expr.arg2 * (expr.arg1 ** (expr.arg2 - 1)))
        else:
            raise NotImplementedError(
                "haven't implemented differentiation of powers in general case"
            )
    else:
        raise TypeError("can't handle {}".format(type(expr)))

    return derivative
