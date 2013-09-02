    This is a literate doctest.
    Run ``python -m doctest -v differentiation.rst`` to test.

Differentiation
===============

>>> from symbolic import Sym
>>> from differentiation import D

>>> x = Sym("x")

>>> D(1, x)
0

>>> D(x, x)
1

>>> D(x + 1, x)
1

>>> D(2 * x, x)
2

>>> D(x ** 2, x)
2 * x
