# Functional Differential Geometry

Working my way through Sussman and Wisdom's Functional Differential Geometry
and implementing it in Python.

The modules should work in both Python 2 and 3.

[![Build Status](http://img.shields.io/travis/jtauber/functional-differential-geometry.svg)](https://travis-ci.org/jtauber/functional-differential-geometry)
[![Coverage Status](http://img.shields.io/coveralls/jtauber/functional-differential-geometry.svg)](https://coveralls.io/r/jtauber/functional-differential-geometry?branch=master)

## tuples.py

Implements the datastructures in the *Tuples* section of *Appendix B*. I
actually really wish Python tuples worked this way :-)

`tuples.rst` explains the module.

## functions.py

Implements the functional capabilities described in the *Functions* section of
*Appendix B*. I guess I wish Python functions worked this way too :-)

`functions.rst` explains the module.

## symbolic.py

Implements some of the symbolic value functionality needed for *Appendix B*.

`symbolic.rst` explains the module.

## simplification.py

Implements some basic simplification of expressions needed for the results of
differentiation to be more readable.

`simplification.rst` explains the module.

## differentiation.py

Very basic symbolic differentiation (still in progress).

`differentiation.rst` explains the module.
