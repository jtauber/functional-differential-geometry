    This is a literate doctest.
    Run ``python -m doctest -v functions.rst`` to test.

Functions
=========

This is based on Appendix B of Functional Differential Geometry by
Gerald Jay Sussman and Jack Wisdom.

We won't be dealing directly with Python functions but instead wrapping them
in our own ``Function`` class.

>>> from functions import Function

The constructor of ``Function`` just takes a Python callable so could be an
inline lambda:

>>> square = Function(lambda x: x**2)
>>> cube = Function(lambda x: x**3)
>>> print(cube(2))
8

or an existing function:

>>> import math
>>> sin = Function(math.sin)

The ``compose`` function takes two ``Function``s and produces a third that is
a composition of the first two.

>>> from functions import compose

>>> h = compose(cube, sin)
>>> h(2) == cube(sin(2))
True

``Function``s can be added, subtracted and multiplied if they take the same
kinds of arguments:

>>> f = square + cube
>>> f(2) == square(2) + cube(2)
True

>>> g = cube * sin
>>> g(2) == cube(2) * sin(2)
True
