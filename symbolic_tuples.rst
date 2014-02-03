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

>>> y = up(1, 2) + "a string!"
Traceback (most recent call last):
    ....
TypeError: addend must be tuple or symbol

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

>>> m = up(1, Sym("n"))
>>> m
up(1, n)

>>> m(n=2)
up(1, 2)

>>> o = up(1, 2) - Sym("p")
>>> o(p=up(0, 1))
up(1, 1)

>>> q = up(1, 2) - "a string!"
Traceback (most recent call last):
    ....
TypeError: subtrahend must be tuple or symbol

>>> r = Sym("s") * up(1, 2)
>>> r(s=2)
up(2, 4)

>>> r(s=down(3, 4))
11

>>> r = up(1, 2) * Sym("s")
>>> r(s=2)
up(2, 4)

>>> r(s=down(3, 4))
11

>>> r(s=up(3, 4))
up(up(3, 6), up(4, 8))

>>> r = 2 * Sym("s")
>>> r(s=up(1, 2))
up(2, 4)

>>> r = Sym("s") * 2
>>> r(s=up(1, 2))
up(2, 4)

>>> r = Sym("s") * Sym("t")
>>> r(s=2, t=up(1, 2))
up(2, 4)

>>> r(s=up(1, 2), t=2)
up(2, 4)

>>> r(s=up(1, 2), t=down(3, 4))
11

>>> r(s=up(1, 2), t=up(3, 4))
up(up(3, 6), up(4, 8))

>>> u = Sym("v") * (Sym("w") + Sym("x"))

>>> u(w=up(1, 2))
(v * (up(1, 2) + x))

>>> u(w=up(1, 2), x=up(3, 4))
(v * up(4, 6))

>>> u(v=down(2, 3))(w=up(1, 2), x=up(3, 4))
26
