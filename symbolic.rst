    This is a literate doctest.
    Run ``python -m doctest -v symbolic.rst`` to test.

Symbolic Values
===============

Symbolic values are those on which arithmetic operations can be performed
without the values being known yet.

>>> from symbolic import Sym

>>> a = Sym("a")
>>> print(a)
a

Expressions can be formed with these symbols and this results in an ``Expr``
object whose evaluation is deferred. 

>>> b = a + 1
>>> c = 2 * a
>>> d = a ** 3

>>> b
(a + 1)

>>> c
(2 * a)

>>> d
(a ** 3)

Such a deferred expression can be evaluated by calling it with keyword
arguments that provide the actual value of any symbolic values.

>>> a(a=5)
5

>>> b(a=5)
6

>>> c(a=5)
10

>>> d(a=5)
125

>>> e = b + c * d
>>> e
((a + 1) + ((2 * a) * (a ** 3)))

>>> e(a=5)
1256

If the necessary symbols are still not provided, the expression remains
deferred:

>>> e(f=5)
((a + 1) + ((2 * a) * (a ** 3)))

>>> x = Sym("x")
>>> y = Sym("y")
>>> z = x + y

>>> z(x=5)
(5 + y)

>>> z(x=5, y=6)
11

>>> z(x=5)(y=7)
12


Numbers
-------

Internally, numbers are wrapped in a ``Num`` class which is also an ``Expr``.

>>> from symbolic import Num

>>> Num(2) == Num(2)
True

>>> Num(2) == 2
True

>>> 2 == Num(2)
True

>>> Num(2) != Num(3)
True

>>> Num(3) + Num(2)
(3 + 2)

>>> Num(3) + 2
(3 + 2)

>>> 2 + Num(3)
(2 + 3)

>>> Num(3) * Num(2)
(3 * 2)

>>> Num(3) * 2
(3 * 2)

>>> 2 * Num(3)
(2 * 3)
