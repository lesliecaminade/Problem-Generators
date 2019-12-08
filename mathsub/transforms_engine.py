import sympy
import math
import random
import wolframalpha
import time

WOLFRAM_NAME = 'ProblemGenerator'
WOLFRAM_APPID = 'VV7LX5-5V58TH8KJX'
client = wolframalpha.Client(WOLFRAM_APPID)


def ask_wolfram(query,**kwargs):
    res = client.query(query)
    print('wolfram response: ', res)
    time.sleep(1)
    try:
        return next(res.results).text
    except:
        print('NO RESULTS')


x, y, z = sympy.symbols('x y z')
a = sympy.symbols('a')
t, s = sympy.symbols('t, s')
     
COE_MAX = 10
POW_MAX = 3
TAYLOR_TERMS = 10

def coe(**kwargs):
    no_zero = False
    for key, value in kwargs.items():
        if key == 'nonzero':
            no_zero = True

    num = random.randint(-COE_MAX, COE_MAX)

    if no_zero and num == 0:
        while num == 0:
            num = random.randint(-COE_MAX, COE_MAX)

    return num
def pow():
    return random.randint(1, POW_MAX)

def random_monomial():
    return coe() * x **pow()
    
def random_taylor_function():
    functions = [
    sympy.E ** random_monomial(),
    random_monomial() * (sympy.E**random_monomial()),
    sympy.cos(random_monomial()),
    sympy.sin(random_monomial()),
    sympy.log(random_monomial()),
    1 / (x**pow()),
    coe() * x**3 + coe() * x**2 + coe()
    ]
    return random.choice(functions)

class Series():
    def __init__(self, terms):
        self.terms = terms

    def print(self, **kwargs):
        terms = len(self.terms)
        for key, value in kwargs.items():
            if key == 'terms':
                terms = value

        _string = ''
        for i in range(terms):
            _string = _string + '(' + str(self.terms[i]) + ') + '
        _string = _string + '...'
        return _string

def taylor(function, center):
    function_derivatives = []
    for i in range(TAYLOR_TERMS):
        function_derivatives.append(function.diff(x, i))

    taylor_terms = []
    for i in range(TAYLOR_TERMS):
        taylor_terms.append(function_derivatives[i] * (x - a)**i / sympy.factorial(i))

    return Series(taylor_terms)

class Taylor_series():
    def __init__(self):
        print('generating ', type(self) )
        self.function = random_taylor_function()
        self.center = abs(coe())
        self.taylor = taylor(self.function, self.center)


def random_laplace_function():
    base_functions = [
    coe() * t,
    coe() * sympy.E**( coe() * t ),
    coe() * sympy.cos( coe() * t ),
    coe() * sympy.sin( coe() * t ),
    coe() * sympy.sinh( coe() * t ),
    coe() * sympy.cosh( coe() * t )
    ]

    base_function = random.choice(base_functions)

    modifications = ['none', 'time_shift', 'frequency_shift', 'frequency_derivative']

    modification = random.choice(modifications)

    if modification == 'none':
        return base_function
    elif modification == 'time_shift':
        return base_function.subs(t, t - coe())
    elif modification == 'frequency_shift':
        return base_function * sympy.E**(coe() * t)
    elif modification == 'frequency_derivative':
        return t**pow() * base_function
    else:
        return None

def laplace(function, **kwargs):
    wolfram = False
    for key, value in kwargs.items():
        if key == 'wolfram':
            wolfram = value

    if wolfram:
        return ask_wolfram(f"""Laplace transform of {function}""")
    else:
        return sympy.laplace_transform(function, t, s, noconds = True)

class Laplace_transform():
    def __init__(self, **kwargs):
        print('generating ', type(self) )
        solve = False
        for key, value in kwargs.items():
            if key == 'solve':
                solve = value
        self.function = random_laplace_function()
        if solve:
            self.laplace = laplace(self.function, wolfram = True)

def random_function_fourier():
    period = coe()

    constant = abs(coe(nonzero = True))
    limits = abs(coe(nonzero = True))
    custom_0 = f"""Piecewise[{{{{{-constant}, {-limits} < x < 0}}, {{{constant}, 0 < x < {limits}}}}} ]"""

    #FourierSeries[Piecewise[{{-4, -5 < x < 0}, {5, 0 < x < 4}}], x, 5]

    func = coe() * x
    custom_1 = f"""Piecewise[{{{{0, -pi < x < -pi/2}}, {{{func}, -pi/2 < x < pi/2}}, {{0 , pi/2 < x < pi}}}}]"""

    slope = abs(coe())
    func_1 = slope * x
    func_2 = - slope * x
    custom_2 = f"""Piecewise[{{{{{func_1}, -pi < x < 0}}, {{{func_2}, 0 < x < pi}}}}]"""

    const = coe()
    custom_3 = f"""Piecewise[{{{{0, -pi < x < 0}}, {{{const}, 0 < x < pi}}}}]"""

    func = coe() * x
    custom_4 = f"""Piecewise[{{{{0, -pi < x < 0}}, {{{func}, 0 < x < pi}}}}]"""

    functions = [custom_0, custom_1, custom_2, custom_3, custom_4]
    function = random.choice(functions)
    return function


def fourier(function, **kwargs):
    full = False
    for key, value in kwargs.items():
        if key == 'full':
            full = value
    return ask_wolfram(f"""FourierSeries[{str(function)}, x, 5]""")

def full_simplify(function):
    return ask_wolfram(f"""FullSimplify[{str(function)}]""")

class Fourier_series():
    def __init__(self, **kwargs):
        print('generating ', type(self) )
        solve = False
        for key, value in kwargs.items():
            if key == 'solve':
                solve = value
        self.function = random_function_fourier()
        if solve:
            self.fourier = full_simplify(fourier(self.function))

