
>>> from symbolic import Sym

>>> a = Sym("a")
>>> b = a + 1
>>> c = 2 * a
>>> d = a ** 3

>>> print(a)
a

>>> b
(a + 1)

>>> c
(2 * a)

>>> d
(a ** 3)

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

>>> e(f=5)
((a + 1) + ((2 * a) * (a ** 3)))


>>> x = Sym("x")
>>> y = Sym("y")
>>> z = x + y

>>> z(x=5)
(5 + y)
