import numbers
import operator


class Expr(object):
    def __add__(self, addend):
        return Add(self, addend)
    
    def __radd__(self, addend):
        return Add(addend, self)
    
    def __sub__(self, subtrahend):
        return Sub(self, subtrahend)
    
    def __rsub__(self, minuend):
        return Sub(minuend, self)
    
    def __mul__(self, multiplicand):
        return Mul(self, multiplicand)
    
    def __rmul__(self, multiplicand):
        return Mul(multiplicand, self)
    
    def __pow__(self, exponent):
        return Pow(self, exponent)


class Num(Expr):
    def __init__(self, arg1):
        self.arg1 = arg1
    
    def __repr__(self):
        return repr(self.arg1)
    
    def __call__(self, **kwargs):
        return self.arg1
    
    def __eq__(self, other):
        if isinstance(other, Num) and self.arg1 == other.arg1:
            return True
        elif isinstance(other, numbers.Number) and self.arg1 == other:
            return True
        else:
            return False
    
    def __ne__(self, other):
        return not self == other


class Sym(Expr):
    def __init__(self, name):
        self._name = name
    
    def __repr__(self):
        return self._name
    
    def __call__(self, **kwargs):
        return kwargs.get(self._name, self)


class BinOp(Expr):
    def __init__(self, arg1, arg2):
        self.arg1 = Num(arg1) if isinstance(arg1, numbers.Number) else arg1
        self.arg2 = Num(arg2) if isinstance(arg2, numbers.Number) else arg2
    
    def __repr__(self):
        return "({} {} {})".format(self.arg1, self.opsymbol, self.arg2)
    
    def __call__(self, **kwargs):
        return self.op(self.arg1(**kwargs), self.arg2(**kwargs))


class Add(BinOp):
    opsymbol = "+"
    op = operator.add


class Sub(BinOp):
    opsymbol = "-"
    op = operator.sub


class Mul(BinOp):
    opsymbol = "*"
    op = operator.mul


class Pow(BinOp):
    opsymbol = "**"
    op = operator.pow
