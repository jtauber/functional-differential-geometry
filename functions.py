"""
see ``functions.rst`` for an explanation.
"""


class Function(object):
    def __init__(self, function):
        self._function = function
    
    def __call__(self, *args):
        return self._function(*args)
    
    def __add__(self, other):
        return Function(
            lambda *args: self._function(*args) + other._function(*args)
        )
    
    def __sub__(self, other):
        return Function(
            lambda *args: self._function(*args) - other._function(*args)
        )
    
    def __mul__(self, other):
        return Function(
            lambda *args: self._function(*args) * other._function(*args)
        )


def compose(function1, function2):
    return Function(
        lambda *args: function1._function(
            function2._function(*args)
        )
    )
