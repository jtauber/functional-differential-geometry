    This is a literate doctest.
    Run ``python -m doctest -v symbolic_tuples.rst`` to test.

Symbolic Tuples
===============

Although not covered in Appendix B, tuples should really be symbolic.

>>> from symbolic import Sym
>>> from tuples import up, down

>>> x = Sym("x")
>>> y = up(1, 2) + x
>>> y(x=up(3, 4))
up(4, 6)

>>> a = Sym("a")
>>> b = a + down(3, 4)
>>> b(a=down(1, 2))
down(4, 6)

>>> c = Sym("c")
>>> d = Sym("d")
>>> e = c + d
>>> e(c=up(1, 2), d=up(3, 4))
up(4, 6)

>>> f = Sym("f")
>>> g = 5 * f
>>> g(f=up(2, 3))
up(10, 15)

>>> h = Sym("h")
>>> i = h * 5
>>> i(h=down(2, 3))
down(10, 15)

>>> j = Sym("j")
>>> k = Sym("k")
>>> l = j + k
>>> l(j=up(1, 2), k=down(3,4))
Traceback (most recent call last):
    ....
TypeError: can't add incompatible Tuples
