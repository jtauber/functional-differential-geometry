#!/usr/bin/env python3


"""
This is based on Appendix B of Functional Differential Geometry by
Gerald Jay Sussman and Jack Wisdom.

Tuples come in two types: **up** and **down**. We represent both types as
ordered lists of their components:

>>> up(1, 2)
up(1, 2)

>>> down(1, 2)
down(1, 2)

Two tuples of the same type are equal if they have the same components:

>>> up(1, 2) == up(1, 2)
True

Two tuples of different types, however, are not equal, regardless of their
components:

>>> up(1, 2) == down(1, 2)
False

Tuples of the same type can be added if they have the same number of
components and the result is another tuple of that type with the
components pairwise-added:

>>> up(1, 2) + up(3, 4)
up(4, 6)

>>> down(1, 2) + down(3, 4)
down(4, 6)

You cannot add two tuples of different types:

>>> up(1, 2) + down(3, 4)
Traceback (most recent call last):
    ....
TypeError: can't add incompatible Tuples

Tuples can be nested and addition applies recursively:

>>> up(1, down(2, 3), 4) + up(5, down(6, 7), 8)
up(6, down(8, 10), 12)

A tuple can be subtracted from another of the same type and number of
components:

>>> up(4, 6) - up(3, 4)
up(1, 2)

Tuples support scalar multiplication:

>>> 2 * up(1, 2)
up(2, 4)

Scalar multiplication applies recursively:

>>> 3 * up(6, up(8, 10), 12)
up(18, up(24, 30), 36)

If you multiple two tuples of opposite types but with the same number of
components, the result is the sum of the pairwise-products:

>>> up(1, 2) * down(3, 4)
11

This is called **contraction**.

If you multiple two tuples that cannot be contracted, the result is the
pairwise-product of the first tuple with each component of the second tuple:

>>> up(1, 2) * up(3, 4)
up(up(3, 6), up(4, 8))

Multiplication by contraction applies recursively:

>>> up(6, up(8, 10), 12) * down(2, down(2, 3), 2)
82

The ``ref`` function takes a tuple and one or more indices to follow to
retrieve a component:

>>> ref(up(1, 2, 3), 1)
2

>>> ref(up(up(1, 2), up(3, 4)), 0, 1)
2

The ``component`` function takes one or more indicies and returns a function
that can be used to retrieve the component of a tuple at that path:

>>> i = component(0, 1)
>>> i(up(up(1, 2), up(3, 4)))
2
"""


class Tuple:
    def __init__(self, *components):
        self._components = components
    
    def __getitem__(self, index):
        return self._components[index]
    
    def __len__(self):
        return len(self._components)
    
    def __eq__(self, other):
        if type(self) == type(other) and self._components == other._components:
            return True
        else:
            return False
    
    def __ne__(self, other):
        return not(self.__eq__(other))
    
    def __add__(self, other):
        if type(self) != type(other) or len(self) != len(other):
            raise TypeError("can't add incompatible Tuples")
        return self.__class__(*(s + o for (s, o) in zip(self._components, other._components)))

    def __sub__(self, other):
        if type(self) != type(other) or len(self) != len(other):
            raise TypeError("can't subtract incompatible Tuples")
        return self.__class__(*(s - o for (s, o) in zip(self._components, other._components)))
    
    def __mul__(self, other):
        if not isinstance(other, Tuple):
            return other * self  # defer to __rmul__
        if self._dual != type(other) or len(self) != len(other):
            return other.__class__(*(self * c for c in other._components))
        return sum(s * o for (s, o) in zip(self._components, other._components))
    
    def __rmul__(self, scalar):
        return self.__class__(*(scalar * c for c in self._components))


class UpTuple(Tuple):
    def __repr__(self):
        return "up({})".format(", ".join(str(c) for c in self._components))


class DownTuple(Tuple):
    def __repr__(self):
        return "down({})".format(", ".join(str(c) for c in self._components))


up = UpTuple
down = DownTuple


up._dual = down
down._dual = up


def ref(tup, *indices):
    if indices:
        return ref(tup[indices[0]], *indices[1:])
    else:
        return tup


def component(*indices):
    def _(tup):
        return ref(tup, *indices)
    return _


if __name__ == "__main__":
    import doctest
    doctest.testmod()
