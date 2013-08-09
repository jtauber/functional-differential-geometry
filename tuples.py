#!/usr/bin/env python3


class Tuple:
    def __init__(self, *components):
        self._components = components


class UpTuple(Tuple):
    pass


class DownTuple(Tuple):
    pass


up = UpTuple
down = DownTuple


if __name__ == "__main__":
    v = up("v^0", "v^1", "v^2")
    p = down("p_0", "p_1", "p_2")
    s = up("t", up("x", "y"), down("p_x", "p_y"))
