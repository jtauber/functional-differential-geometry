#!/usr/bin/env python3


class Tuple:
    def __init__(self, *components):
        self._components = components
    
    def __getitem__(self, index):
        return self._components[index]


class UpTuple(Tuple):
    pass


class DownTuple(Tuple):
    pass


up = UpTuple
down = DownTuple


def ref(tup, *indices):
    if indices:
        return ref(tup[indices[0]], *indices[1:])
    else:
        return tup


if __name__ == "__main__":
    v = up("v^0", "v^1", "v^2")
    p = down("p_0", "p_1", "p_2")
    s = up("t", up("x", "y"), down("p_x", "p_y"))
    assert ref(up("a", "b", "c"), 1) == "b"
    assert ref(up(up("a", "b"), up("c", "d")), 0, 1) == "b"
