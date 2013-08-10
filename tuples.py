#!/usr/bin/env python3


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
    v = up("v^0", "v^1", "v^2")
    p = down("p_0", "p_1", "p_2")
    s = up("t", up("x", "y"), down("p_x", "p_y"))
    assert ref(up("a", "b", "c"), 1) == "b"
    assert ref(up(up("a", "b"), up("c", "d")), 0, 1) == "b"
    assert component(0, 1)(up(up("a", "b"), up("c", "d"))) == "b"
    assert repr(up(1, 2)) == "up(1, 2)"
    assert repr(down(1, 2)) == "down(1, 2)"
    assert up(1, 2) == up(1, 2)
    assert up(1, 2) != down(1, 2)
    assert up(1, 2) + up(3, 4) == up(4, 6)
    assert down(1, 2) + down(3, 4) == down(4, 6)
    try:
        up(1, 2) + down(3, 4)
        assert False
    except TypeError:
        pass
    assert up(1, up(2, 3), 4) + up(5, up(6, 7), 8) == up(6, up(8, 10), 12)
    assert up(4, 6) - up(3, 4) == up(1, 2)
    assert 2 * up(1, 2) == up(2, 4)
    assert 3 * up(6, up(8, 10), 12) == up(18, up(24, 30), 36)
    assert up(1, 2) * down(3, 4) == 11
    assert up(1, 2) * up(3, 4) == up(up(3, 6), up(4, 8))
