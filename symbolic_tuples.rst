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
