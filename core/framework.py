import sympy
import itertools
from sympy import latex
from multipledispatch import dispatch
from rpn_to_infix import *

#prec_dict =  {'^':4, '*':3, '/':3, '+':2, '-':2}
#assoc_dict = {'^':1, '*':0, '/':0, '+':0, '-':0}
class TexMathOp(object):
    """basic math ops for symbolic objects"""
    def __init__(self, arg):

        if type(arg) == TexMathOp:
            arg = arg.base_name
        else:
            pass
        
        self.base_name = arg
        import sympy
        self.sym = sympy.symbols(self.base_name)

    def __add__(self, other):

        if type(other) in classes:
            return TexExpr(self.get_val() + other.get_val(), 
                           [*self.get_polis(), *other.get_polis(), '+'])#self.get_str() + other.get_str() + ['+'])
        else:
            return TexExpr(self.get_val() + sympy.sympify(other), 
                           self.get_str() + [sympy.sympify(other)] + ['+'])

    def __pow__(self, other):
        if type(other) in classes:
            return TexExpr(self.get_val() ** other.get_val(), 
                           [*self.get_polis(), *other.get_polis(), '**'])#self.get_str() + other.get_str() + ['**'])
        else:
            return TexExpr(self.get_val() ** sympy.sympify(other), 
                           self.get_str() + [sympy.sympify(other)] + ['**'])

    def __sub__(self, other):
        if type(other) in classes:
            return TexExpr(self.get_val() - other.get_val(), 
                           [*self.get_polis(), *other.get_polis(), '-'])#self.get_str() + other.get_str() + ['-'])
        else:
            return TexExpr(self.get_val() + sympy.sympify(other), 
                           self.get_str() + [sympy.sympify(other)] + ['-'])

    def __mul__(self, other):
        if type(other) in classes:
            return TexExpr(self.get_val() * other.get_val(), 
                           [*self.get_polis(), *other.get_polis(), '*'])#self.get_str() + other.get_str() + ['*'])
        else:
            return TexExpr(self.get_val() * sympy.sympify(other), 
                           self.get_str() + [sympy.sympify(other)] + ['*'])

    def __truediv__(self, other):
        if type(other) in classes:
            return TexExpr(self.get_val() / other.get_val(), 
                           [*self.get_polis(), *other.get_polis(), '/'])#self.get_str() + other.get_str() + ['/'])
        else:
            return TexExpr(self.get_val() / sympy.sympify(other), 
                           self.get_str() + [sympy.sympify(other)] + ['/'])

    def __floordiv__(self, other):
        if type(other) in classes:
            return TexExpr(self.get_val() // other.get_val(), 
                           [*self.get_polis(), *other.get_polis(), '//'])#self.get_str() + other.get_str() + ['//'])
        else:
            return TexExpr(self.get_val() // sympy.sympify(other), 
                           self.get_str() + [sympy.sympify(other)] + ['//'])

    def __mod__(self, other):
        if type(other) in classes:
            return TexExpr(self.get_val() % other.get_val(), 
                           [*self.get_polis(), *other.get_polis(), '%'])#self.get_str() + other.get_str() + ['%'])
        else:
            return TexExpr(self.get_val() % sympy.sympify(other), 
                           self.get_str() + [sympy.sympify(other)] + ['%'])

    def __rshift__(self, other):
        if type(other) in classes:
            return TexExpr(self.get_val() >> other.get_val(), 
                           [*self.get_polis(), *other.get_polis(), '>>'])#self.get_str() + other.get_str() + ['>>'])
        else:
            return TexExpr(self.get_val() >> sympy.sympify(other), 
                           self.get_str() + [sympy.sympify(other)] + ['>>'])

    def __lshift__(self, other):
        if type(other) in classes:
            return TexExpr(self.get_val() << other.get_val(), 
                           [*self.get_polis(), *other.get_polis(), '<<'])#self.get_str() + other.get_str() + ['<<'])
        else:
            return TexExpr(self.get_val() << sympy.sympify(other), 
                           self.get_str() + [sympy.sympify(other)] + ['<<'])

    def __and__(self, other):
        if type(other) in classes:
            return TexExpr(self.get_val() & other.get_val(), 
                           [*self.get_polis(), *other.get_polis(), '&'])#self.get_str() + other.get_str() + ['&'])
        else:
            return TexExpr(self.get_val() & sympy.sympify(other), 
                           self.get_str() + [sympy.sympify(other)] + ['&'])

    def __or__(self, other):
        if type(other) in classes:
            return TexExpr(self.get_val() | other.get_val(), 
                           [*self.get_polis(), *other.get_polis(), '|'])#self.get_str() + other.get_str() + ['|'])
        else:
            return TexExpr(self.get_val() | sympy.sympify(other), 
                           self.get_str() + [sympy.sympify(other)] + ['|'])

    def __xor__(self, other):
        if type(other) in classes:
            return TexExpr(self.get_val() ^ other.get_val(), 
                           [*self.get_polis(), *other.get_polis(), '^'])#self.get_str() + other.get_str() + ['^'])
        else:
            return TexExpr(self.get_val() ^ sympy.sympify(other), 
                           self.get_str() + [sympy.sympify(other)] + ['^'])

    def __lt__(self, other):
        if type(other) in classes:
            return TexExpr(self.get_val() < other.get_val(), 
                           [*self.get_polis(), *other.get_polis(), '<'])#self.get_str() + other.get_str() + ['<'])
        else:
            return TexExpr(self.get_val() < sympy.sympify(other), 
                           self.get_str() + [sympy.sympify(other)] + ['<'])

    def __le__(self, other):
        if type(other) in classes:
            return TexExpr(self.get_val() <= other.get_val(), 
                           [*self.get_polis(), *other.get_polis(), '<='])#self.get_str() + other.get_str() + ['<='])
        else:
            return TexExpr(self.get_val() <= sympy.sympify(other), 
                           self.get_str() + [sympy.sympify(other)] + ['<='])

    def __gt__(self, other):
        if type(other) in classes:
            return TexExpr(self.get_val() > other.get_val(), 
                           [*self.get_polis(), *other.get_polis(), '>'])#self.get_str() + other.get_str() + ['>'])
        else:
            return TexExpr(self.get_val() > sympy.sympify(other), 
                           self.get_str() + [sympy.sympify(other)] + ['>'])

    def __ge__(self, other):
        if type(other) in classes:
            return TexExpr(self.get_val() >= other.get_val(), 
                           [*self.get_polis(), *other.get_polis(), '>='])#self.get_str() + other.get_str() + ['>='])
        else:
            return TexExpr(self.get_val() >= sympy.sympify(other), 
                           self.get_str() + [sympy.sympify(other)] + ['>='])

    def __eq__(self, other):
        if type(other) in classes:
            return TexExpr(self.get_val() == other.get_val(), 
                           [*self.get_polis(), *other.get_polis(), '=='])#self.get_str() + other.get_str() + ['=='])
        else:
            return TexExpr(self.get_val() == sympy.sympify(other), 
                           self.get_str() + [sympy.sympify(other)] + ['=='])

    def __ne__(self, other):
        if type(other) in classes:
            return TexExpr(self.get_val() != other.get_val(), 
                           [*self.get_polis(), *other.get_polis(), '!='])#self.get_str() + other.get_str() + ['!='])
        else:
            return TexExpr(self.get_val() != sympy.sympify(other), 
                           self.get_str() + [sympy.sympify(other)] + ['!='])

    def __neg__(self):
        return TexExpr(-self.get_val(), [*self.get_polis(), '-u'])#self.get_str() + ['-u'])

    def __pos__(self):
        return TexExpr(+self.get_val(), [*self.get_polis(), '+u'])#self.get_str() + ['+u'])

    def __invert__(self):
        return TexExpr(~self.get_val(), [*self.get_polis(), '~u'])#self.get_str() + ['~u'])

class TexSymbol(TexMathOp):
    """
    Class, meant to create and use different kind of symbols.\n
    ### Init args:
        arg: str - symbol to be represented
    ### Examples:\n 
        x = TexSymbol('x')
    """

    def hat(self):
        
        self.sym = sympy.symbols(self.base_name + 'hat')
        return self

    def check(self):
        self.sym = sympy.symbols(self.base_name + 'check')
        return self

    def tilde(self):
        self.sym = sympy.symbols(self.base_name + 'tilde')
        return self

    def acute(self):
        self.sym = sympy.symbols(self.base_name + 'acute')
        return self

    def grave(self):
        self.sym = sympy.symbols(self.base_name + 'grave')
        return self

    def dot(self):
        self.sym = sympy.symbols(self.base_name + 'dot')
        return self

    def ddot(self):
        self.sym = sympy.symbols(self.base_name + 'ddot')
        return self

    def dddot(self):
        self.sym = sympy.symbols(self.base_name + 'dddot')
        return self

    def ddddot(self):
        self.sym = sympy.symbols(self.base_name + 'ddddot')
        return self

    def breve(self):
        self.sym = sympy.symbols(self.base_name + 'breve')
        return self

    def bar(self):
        self.sym = sympy.symbols(self.base_name + 'bar')
        return self

    def vec(self):
        self.sym = sympy.symbols(self.base_name + 'vec')
        return self

    def get_str(self):
        return [self.base_name]

    def get_val(self):
        return self.sym
    
    def get_polis(self):
        return [self]

    def __repr__(self):
        return self.sym.__repr__()

    def __str__(self):
        return self.sym.__str__()


class TexExpr(TexMathOp):
    """
    Class, generated after any arithmetic operation to basic object (TexSymbol, TexFraction etc.). Less likely to be 
    initialized directly by user then by operations with basic objects.\n
    ### Init args:
        ```arg: str``` - expression to be represented
    ### Examples:\n 
    ```
        x = TexSymbol('x')
        y = TexSymbol('y')
        expr1 = (x + y*2)

        expr2 = TexExpr("x + y*2")   # may lead to some errors
    ```
    """
    
    def __init__(self, arg, str_=None):
        #super(TexExpr, self).__init__()

        if type(arg) == str:
            self.expr = sympy.sympify(arg)
        else:
            self.expr = arg
        self.polis = []
        if str_ != None:
            self.polis += str_
        self._strict = None

    def get_str(self):
        return self.polis

    def get_val(self):
        return self.expr
    
    def get_polis(self):
        return self.polis

    def __repr__(self):
        return self.expr.__repr__()

    def __str__(self):
        return self.expr.__str__()
    
    def float(self, lim=None):

        if (type(self.expr) == int or type(self.expr) == float or 
            type(self.expr) == sympy.core.numbers.Float or
            type(self.expr) == sympy.core.numbers.Integer):
            return TexNumber(self.expr).float(lim)
        
        else:
            return None ##

    def strict(self):
        polis = []
        self.is_strict = True
        for x in self.polis:
            if type(x) in classes:
                polis.append(latex(x))
            else:
                polis.append(x)
        self._strict = rpn_to_infix(polis)
        return self
        
    def diff(self, args=None):
        return sympy.diff(self.expr, *args)
        
    #def __call__(self, x):
    #    return self.expr.subs()

class TexNumber(TexMathOp):
    """
    Class, representing numbers.
    ### Init args:
        ```arg: str``` - number as string or any python type
    ### Examples:\n 
    ```
        x = TexNumber(1)
        y = TexSymbol('1.5431')
        y.float(2)  # 1.54
    ```
    """
    def __init__(self, arg):
        #super(TexNumber, self).__init__()

        self.num = sympy.sympify(arg)
        self.str = str(self.num)

    def get_str(self):
        return [self.str]

    def get_val(self):
        return self.num

    def float(self, lim=None):
        if lim == None:
            return float(self.num)
        else:
            return float("{:.2f}".format(self.num, lim=lim))
        
    def get_polis(self):
        return [self]

    def __repr__(self):
        return self.num.__repr__()

    def __str__(self):
        return self.num.__str__()

class TexFraction(TexMathOp):
    """
    Class, representing fractions.
    ### Init args:
        ```arg: str``` - most likely to be a string, or TexObject
    ### Examples:\n 
    ```
        x = TexFraction('3/4')
    ```
    """
    def __init__(self, arg):
        #super(TexNumber, self).__init__()

        self.num = sympy.sympify(arg)
        self.str = str(self.num)
        self._slash = False

    def get_str(self):
        return [self.str]

    def get_val(self):
        return self.num

    def slash(self):
        """требует подключения \\usepackage{xfrac}"""
        self._slash = True
        return self

    def float(self, lim=None):
        if type(self.num) != sympy.core.numbers.Rational:
            # сделать нормальное сообщение об ошибке
            print('TexFraction.float(): incompatible type, expected Rational, got: ', type(self.num))
            exit(1)
        if lim == None:
            return float(self.num)
        else:
            return float("{:.2f}".format(self.num, lim=lim))

    def line(self):
        self._slash = False
        return self
    
    def get_polis(self):
        return [self]

    def __repr__(self):
        return self.num.__repr__()

    def __str__(self):
        return self.num.__str__()

class TexMatrix(TexMathOp):
    """
    Class, representing matrices.
    ### Init args:
        ```arg: list``` - list, may be string
    ### Examples:\n 
    ```
        x1 = TexMatrix('[[1, -1], [3, 4]]')
        x2 = TexMatrix([[1, 0], [0, 0]])
    ```
    """
    def __init__(self, arg):
        #super(TexNumber, self).__init__()

        self.mat = sympy.Matrix(sympy.sympify(str(arg)))
        self.str = str(self.mat)            ##проблема
        self.brackets = '[]'

    def get_str(self):
        return [self.str]

    def get_val(self):
        return self.mat
    
    def round_brackets(self):
        self.brackets = '()'
        return self
    
    def straight_brackets(self):
        self.brackets = '||'
        return self
    
    def get_polis(self):
        return [self]
    
    def __repr__(self):
        return self.mat.__repr__()

    def __str__(self):
        return self.mat.__str__()
    

class TexFunction(TexMathOp):
    """
    Class, representing functions.
    ### Init args:
        ```name = 'f': str```\n
        ```f_args = None: list[str]```\n
        ```val = None: str```
    ### Examples:\n 
    ```
        F = TexFunction(name='F', f_args=['x'], val='sin(x)')
        G = TexFunction(name='G')
    ```
    """
    def __init__(self, name = 'f', f_args = None, val = None):

        self.name = name
        self.f_args = f_args
        self.d_cnt = 0
        self.val = val

        if val == None:
            self.ftype = 'unvalued'
            if f_args != None:
                self.func = sympy.Function(name)(*f_args)
            else:
                self.func = sympy.Function(name)
        else:
            self.ftype = 'valued'
            self.func = TexExpr(val)

        self.str = str(self.func)

    def drop_arg(self):
        return sympy.Function(self.name)
    
    def diff(self, args=None):
        if args == None: args = self.f_args
        return self.func.diff(*args)
    
    def d(self, n=1):
        self.d_cnt = n
        return self
        
    def get_str(self):
        return [self.str]

    def get_val(self):
        return self.func
    
    def get_polis(self):
        return [self]
    
    def __repr__(self):
        return self.func.__repr__()

    def __str__(self):
        return self.func.__str__()
    
    def __call__(self, x):
    
        return TexExpr(self.val).expr.subs(self.f_args[0], x)


classes = [TexFraction, TexNumber, TexExpr, TexSymbol, TexMatrix, TexFunction]

"""
to do:
для выражений, сделать так: по полису строить само выражение
пока нельзя влиять на вывод latex(TexExpr) (не учитывается например TexFraction.slash())
пока нельзя делать int + TexObject (не определены мат. операции для int и др типов), наоборот можно
наверное, надо сделать класс TexExprStrict(TexExpr), который будет содержать выражение в строгом порядке,
    причем генерить код латеха надо будет вручную скорее всего
"""

@dispatch(object)
def latex(x):
    return sympy.latex(x)

@dispatch(TexSymbol)
def latex(x):
    return sympy.latex(x.sym)

@dispatch(TexExpr)
def latex(x):
    if x._strict:
        return x._strict.replace('*', '').replace('(', '\\left(').replace(')', '\\right)')
    else:
        text = sympy.sympify(x.get_val())
    return sympy.latex(text)

@dispatch(TexFraction)
def latex(x):
    text = sympy.latex(x.num)
    if x._slash:
        text = text.replace('\\frac', '\\sfrac')
    return text

@dispatch(TexMatrix)
def latex(x):
    
    if x.brackets == '()':
        return sympy.latex(x.get_val(), mat_delim='(', mat_str='matrix')
    elif x.brackets == '||':
        return sympy.latex(sympy.Determinant(sympy.Matrix(x.get_val())), mat_delim='')

    return sympy.latex(x.get_val())

@dispatch(TexFunction)
def latex(x):

    if x.d_cnt:
        # может быть просто функция, но если название функции из 2 или больше букв - operatorname
        str_ = sympy.latex(x.func)
        tmp = str_.find(x.name) + len(x.name) - 1

        if x.d_cnt > 3:
            diff_deg = "^{(" + str(x.d_cnt) + ")}"
        else:
            diff_deg = "'"*x.d_cnt

        if tmp + 1 < len(str_) and str_[tmp + 1] == '}':
            return str_[:tmp + 2] + diff_deg + str_[tmp + 2:]
        else:
            return str_[:tmp + 1] + diff_deg + str_[tmp + 1:]
    
    return sympy.latex(x.func)


