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

>>> simplify((0 * x) + (1 * 2))
2

>>> from symbolic import Num
>>> simplify(Num(2) - Num(1))
1

>>> simplify(Num(1) * Num(2))
2

>>> simplify(Num(1) + Num(2))
3

>>> simplify(x ** 1)
x

>>> simplify(x - 0)
x

>>> simplify(0 - x)
(-1 * x)

>>> simplify("can't simplify a string")
Traceback (most recent call last):
    ....
TypeError: can't handle <type 'str'>

