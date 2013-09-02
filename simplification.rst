    This is a literate doctest.
    Run ``python -m doctest -v simplification.rst`` to test.

Simplification
==============

Only very basic simplification is supported at the moment. Just enough for
basic differentiation to work.

>>> from simplification import simplify

>>> from symbolic import Sym
>>> x = Sym("x")

>>> x + 0
(x + 0)

>>> simplify(x + 0)
x

>>> simplify(0 * x)
0

>>> simplify(x * 0)
0

>>> simplify(1 * x)
x

>>> simplify(x * 1)
x

>>> simplify(1 * 2)
2

>>> simplify((0 * x) + (1 * 2))
2
