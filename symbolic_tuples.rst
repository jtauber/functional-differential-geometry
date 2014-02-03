    This is a literate doctest.
    Run ``python -m doctest -v symbolic_tuples.rst`` to test.

Symbolic Tuples
===============

Although not covered in Appendix B, tuples should really be symbolic.

>>> from symbolic import Sym
>>> from tuples import up, down

>>> y = up(1, 2) + Sym("x")
>>> y(x=up(3, 4))
up(4, 6)

>>> b = Sym("a") + down(3, 4)
>>> b(a=down(1, 2))
down(4, 6)

>>> e = Sym("c") + Sym("d")
>>> e(c=up(1, 2), d=up(3, 4))
up(4, 6)

>>> g = 5 * Sym("f")
>>> g(f=up(2, 3))
up(10, 15)

>>> i = Sym("h") * 5
>>> i(h=down(2, 3))
down(10, 15)

>>> l = Sym("j") + Sym("k")
>>> l(j=up(1, 2), k=down(3,4))
Traceback (most recent call last):
    ....
TypeError: can't add incompatible Tuples
