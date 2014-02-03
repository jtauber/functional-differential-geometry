"""
see ``tuples.rst`` for an explanation.
"""

from symbolic import Expr, Add, Sub, Mul


class Tuple(Expr):
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
        if isinstance(other, Tuple):
            if type(self) != type(other) or len(self) != len(other):
                raise TypeError("can't add incompatible Tuples")
            else:
                return self.__class__(
                    *(s + o for (s, o) in zip(
                        self._components, other._components))
                )
        elif isinstance(other, Expr):
            return Add(self, other)
        else:
            raise TypeError("addend must be tuple or symbol")

    def __sub__(self, other):
        if isinstance(other, Tuple):
            if type(self) != type(other) or len(self) != len(other):
                raise TypeError("can't subtract incompatible Tuples")
            else:
                return self.__class__(
                    *(s - o for (s, o) in zip(
                        self._components, other._components))
                )
        elif isinstance(other, Expr):
            return Sub(self, other)
        else:
            raise TypeError("subtrahend must be tuple or symbol")

    def __mul__(self, other):
        if isinstance(other, Tuple):
            if self._dual != type(other) or len(self) != len(other):
                return other.__class__(*(self * c for c in other._components))
            else:
                return sum(
                    s * o for (s, o) in zip(
                        self._components, other._components)
                )
        elif isinstance(other, Expr):
            return Mul(self, other)
        else:
            return other * self  # defer to __rmul__

    def __rmul__(self, scalar):
        return self.__class__(*(scalar * c for c in self._components))

    def __call__(self, **kwargs):
        return self.__class__(*(
            (c(**kwargs) if isinstance(c, Expr) else c)
            for c in self._components
        ))


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
