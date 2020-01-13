from generator import random_handler as ran
import sympy as sym
import math
import random
from generator import constants_conversions as c
from num2words import num2words
from mathsub import analytic_geometry_engine

x, y, z = sym.symbols('x y z', real = True)#generic variables
MAX_COE = 9
MAX_POWER = 3
POLY_TERMS_MIN = 4
POLY_TERMS_MAX = 6

MULTIVARIABLE_POWER_MAX = 3
MULTIVARIABLE_COE_MAX = 9
MULTIVARIABLE_TERMS_MAX = 5

X_RANGE = 10
Y_RANGE = 10


SHORT_POLYNOMIAL_TYPES = ['quadratic-linear-constant', 'linear-constant', 'quadratic-constant', 'linear', 'quadratic-linear']

def random_coeff():
    num = 0
    while num == 0:
        num = random.randint(-MAX_COE, MAX_COE)
    return num

def random_positive_coeff():
    num = 0
    while num == 0:
        return random.randint(0, MAX_COE)
    return num


def random_power():
    return random.randint(0, MAX_POWER)

def random_fraction():
    choices = ['positive', 'negative']

    choice = random.choice(choices)

    if choice == 'positive':
        return random_positive_fraction()
    elif choice == 'negative':
        return random_negative_fraction()
    else:
        raise InternalError('invalid input from function itself')

def random_negative_fraction():
    numerator = random.randint(1,int(MAX_COE/2))
    denominator = numerator + random.randint(1, int(MAX_COE/2))
    return sym.Rational(- numerator, denominator)

def random_positive_fraction():
    numerator = random.randint(1,int(MAX_COE/2))
    denominator = numerator + random.randint(1, int(MAX_COE/2))
    return sym.Rational(numerator, denominator)

def random_inequality(expression1, expression2):
    inequality = random.randint(0, 3)

    if inequality == 0:
        return expression1 > expression2
    elif inequality == 1:
        return expression1 < expression2
    elif inequality == 2:
        return expression1 >= expression2
    else:
        return expression1 <= expression2

class Inequality():
    def __init__(self):
        pass

    def init_expression(self, expression):
        self.expression = expression

    def init_expression_random_inequality(self, expression1, expression2):
        self.expression = random_inequality(expression1, expression2)

    def solve(self):
        expression = self.expression
        solution_set = sym.solveset(expression, x, domain = sym.S.Reals)
        return solution_set



class Polynomial():
    def __init__(self):
        pass

    def init_coeff(self,*args):
        self.expression = 0 * x
        args.reverse()
        for i in range(len(args)):
            self.expression = self.expression + args[i] * x**i

    def init_roots(self, *args):
        expression = 1
        for arg in args:
            expression = expression * (x - arg)

        self.expression = expression

    def init_expression(self, expression):
        self.expression = expression

    def init_random(self, terms = None, variables = None):
        expression = 0 * x

        if terms == None:
            terms = random.randint(POLY_TERMS_MIN,POLY_TERMS_MAX)

        if variables == None:
            variables = 1

        tryagain = True
        while tryagain:
            try:
                if variables == 1:
                    for i in range(terms):
                        expression = expression + random_coeff() * x**i

                if variables == 2:
                    for i in range(terms):
                        expression = expression + random_coeff() * x**random_power() * y**random_power()

                if variables == 3:
                    for i in range(terms):
                        expression = expression + random_coeff() * x**random_power() * y**random_power() * z**random_power()

                self.expression = expression
                tryagain = False
            except:
                tryagain = True

        return self.expression


    def degree(self):
        self.expression = sym.Poly(self.expression)
        self.total_degree = self.expression.total_degree()
        return self.total_degree

    def sum_of_the_roots(self):
        self.expression = sym.Poly(self.expression)
        #determines the sum of the roots via the vieta's formula
        coefficients = self.expression.all_coeffs()

        sum_of_the_roots = (-1) * (coefficients[1]/coefficients[0])
        return sum_of_the_roots

    def product_of_the_roots(self):
        self.expression = sym.Poly(self.expression)
        #determines the product of the roots via the vieta's formula
        coefficients = self.expression.all_coeffs()
        degree = self.expression.total_degree()
        product_of_the_roots = (-1)**degree * (coefficients[degree]/coefficients[0])

        return product_of_the_roots

    def substitute(self, value):
        self.expression = sym.Poly(self.expression)
        return self.expression.subs(x, value)

    def coefficients(self):
        polynomial = sym.Poly(self.expression)
        return polynomial.all_coeffs()

    def point(self):
        x1 = random.randint(-X_RANGE, X_RANGE)
        y1 = self.expression.subs(x, x1)
        point = analytic_geometry_engine.Point()
        point.init_define(x1, y1)
        return point

class Linear(Polynomial):
    def __init__(self, *args):
        if args:
            self.expression = args[0]

    def init_random(self):
        A = 0
        while A == 0:
            A = random_coeff()

        B = random_coeff()
        self.a = A
        self.b = B
        self.expression = A * x + B
        return self.expression

    def init_coeff(self, a, b):
        self.a = a
        self.b = b
        self.expression = 0 * x
        self.expression = sym.Poly(a * x + b)
        return self.expression.as_expr()

    def inverse(self):
        equation = sym.Eq(x, self.expression.subs(x, y))
        print(equation)
        solution_set = sym.solveset(equation, y)
        print(solution_set)
        solution_list = list(solution_set)
        new = Linear()
        new.init_expression(solution_list[0])
        return new

    def root(self):
        return  - self.b/self.a


class Quadratic(Polynomial):
    def __init__(self):
        pass

    def init_random(self):
        A = 0
        while A == 0:
            A = random_coeff()
        B = random_coeff()
        C = random_coeff()
        self.expression = sym.Poly(A* x**2 + B * x +C)
        return self.expression.as_expr()

    def init_coeff(self, a, b, c):
        self.expression = 0 * x
        self.expression = sym.Poly(a * x**2 + b * x  + c)
        return self.expression.as_expr()


    def init_roots(self, r1, r2):
        self.expression = sym.Poly((x - r1) * (x - r2))
        return self.expression.as_expr()

    def discriminant(self):
        return self.expression.discriminant()


class ShortPolynomial():
    def __init__(self):
        pass

    def init_types(self, types):
        A = 0
        B = 0
        C = 0
        D = 0
        if types == 'quadratic-linear-constant':
            while A == 0:
                A = random_coeff()
            while B == 0:
                B = random_coeff()
            while C == 0:
                C = random_coeff()

        if types == 'quadratic-linear':
            while A == 0:
                A = random_coeff()
            while B == 0:
                B = random_coeff()

        if types == 'quadratic-constant':
            while A == 0:
                A = random_coeff()
            while C == 0:
                C = random_coeff()

        if types == 'linear-constant':
            while B == 0:
                B = random_coeff()
            while C == 0:
                C = random_coeff()

        if types == 'linear':
            while B == 0:
                B = random_coeff()

        if types == 'cubic-linear':
            while B == 0:
                B = random_coeff()
            while D == 0:
                D = random_coeff()

        if types == 'cubic-constant':
            while B == 0:
                C = random_coeff()
            while D == 0:
                D = random_coeff()


        self.expression = D * x**3 + A * x**2 + B * x + C

        return self.expression

    def init_random(self):

        types = random.choice(SHORT_POLYNOMIAL_TYPES)

        A = 0
        B = 0
        C = 0
        D = 0

        if types == 'quadratic-linear-constant':
            while A == 0:
                A = random_coeff()
            while B == 0:
                B = random_coeff()
            while C == 0:
                C = random_coeff()

        if types == 'quadratic-linear':
            while A == 0:
                A = random_coeff()
            while B == 0:
                B = random_coeff()

        if types == 'quadratic-constant':
            while A == 0:
                A = random_coeff()
            while C == 0:
                C = random_coeff()

        if types == 'linear-constant':
            while B == 0:
                B = random_coeff()
            while C == 0:
                C = random_coeff()

        if types == 'cubic-linear':
            while B == 0:
                B = random_coeff()
            while D == 0:
                D = random_coeff()

        if types == 'cubic-constant':
            while B == 0:
                C = random_coeff()
            while D == 0:
                D = random_coeff()

        self.expression = D * x**3 + A * x**2 + B * x + C

        return self.expression


class MixedPowerPolynomial():
    def __init__(self):
        self.expression = 0*x

    def init_random(self):
        terms = random.randint(POLY_TERMS_MIN, POLY_TERMS_MAX)
        for i in range(terms):
            self.expression = self.expression + random_coeff() * x**(random_fraction())
            return self.expression

class NegativePowerPolynomial():
    def __init__(self):
        self.expression = 0*x

    def init_random(self):
        terms = random.randint(POLY_TERMS_MIN, POLY_TERMS_MAX)
        for i in range(terms):
            self.expression = self.expression + random_coeff() * x**(-random_coeff())
            return self.expression

class PositiveFractionPowerPolynomial():
    def __init__(self):
        self.expression = 0 * x
        

    def init_random(self):
        terms = random.randint(POLY_TERMS_MIN, POLY_TERMS_MAX)
        for i in range(terms):
            self.expression = self.expression + random_coeff() * x**(random_positive_fraction())
            return self.expression

class NegativeFractionPowerPolynomial():
    def __init__(self):
        self.expression = 0*x
        

    def init_random(self):
        terms = random.randint(POLY_TERMS_MIN, POLY_TERMS_MAX)

        for i in range(terms):
            self.expression = self.expression + random_coeff() * x**(random_negative_fraction())
            return self.expression

class Rational():
    def __init__(self):
        self.expression = 0*x

    def init_random(self):
        numerator = ShortPolynomial()
        denominator = ShortPolynomial()
        numerator.init_random()
        denominator.init_random()

        self.expression = numerator.expression / denominator.expression

        self.expression_variation_1 = numerator.expression / sym.sqrt(denominator.expression)

        return self.expression

class DiscreteFunction():
    def __init__(self):
        pass

    def init_random(self, start, end, step):
        input_values = []
        output_values = []

        for i in range(start, end + 1, step):
            input_values.append(i)
            output_values.append(random.randint(start, end + 1))

        self.input_values = input_values
        self.output_values = output_values

    def substitute(self, input_value):
        for i in range(len(self.input_values)):
            if self.input_values[i] == input_value:
                return self.output_values[i]

class Piecewise():
    def __init__(self):
        pass

    def init_random(self, parts):
        boundary_points = []
        for i in range(parts - 1):
            boundary_points.append(random_coeff())

        #pick a random type of equation
        expressions = []
        for i in range(parts):
            a = Linear()
            b = Quadratic()
            a.init_random()
            b.init_random()
            possible_expressions = [a.expression.as_expr(), b.expression.as_expr(), random_coeff()]
            expressions.append(random.choice(possible_expressions))

        #create the piecewise function
        if parts == 2:
            expression = sym.Piecewise((expressions[0], x < boundary_points[0]), (expressions[1], x >= boundary_points[0]))

        self.expression = expression
        return self.expression

    def substitute(self, value):
        return self.expression.subs(x, value)
        
class Bivariable():
    def __init__(self):
        self.expression = 0 * x
        pass

    def init_random(self, **kwargs):
        terms = random.randint(1, MULTIVARIABLE_TERMS_MAX)
        
        for key, value in kwargs.items():
            if key == 'terms':
                terms = value

        for i in range(terms):
            again = True
            while again:
                powerx = random.randint(0, MULTIVARIABLE_POWER_MAX)
                powery = random.randint(0, MULTIVARIABLE_POWER_MAX)

                if not( powerx == 0 and powery == 0):
                    again = False

            self.expression = self.expression + random_coeff() * x**powerx * y ** powery

        self.expression = self.expression + random.randint(-MAX_COE, MAX_COE)

        return self.expression

    def init_random_conic_section(self):
        CONIC_SECTIONS = ['circle', 'ellipse', 'parabola', 'hyperbola']
        conic_section = random.choice(CONIC_SECTIONS)
        if conic_section == 'circle':
            self.conic_section = analytic_geometry_engine.Circle()
        elif conic_section == 'ellipse':
            self.conic_section = analytic_geometry_engine.Ellipse()
        elif conic_section == 'parabola':
            self.conic_section = analytic_geometry_engine.Parabola()
        elif conic_section == 'hyperbola':
            self.conic_section = analytic_geometry_engine.Hyperbola()
        else:
            raise InternalError('invalid conic section')

        self.conic_section.init_random()
        self.expression = self.conic_section.general
        self.expression_string = f"""{self.conic_section.general_string}"""

        return self.conic_section

    def init_random_conic_section_no_hyperbola(self):
        CONIC_SECTIONS = ['circle', 'ellipse', 'parabola']
        conic_section = random.choice(CONIC_SECTIONS)
        if conic_section == 'circle':
            self.conic_section = analytic_geometry_engine.Circle()
        elif conic_section == 'ellipse':
            self.conic_section = analytic_geometry_engine.Ellipse()
        elif conic_section == 'parabola':
            self.conic_section = analytic_geometry_engine.Parabola()
        elif conic_section == 'hyperbola':
            self.conic_section = analytic_geometry_engine.Hyperbola()
        else:
            raise InternalError('invalid conic section')

        self.conic_section.init_random()
        self.expression = self.conic_section.general
        self.expression_string = f"""{self.conic_section.general_string}"""

        return self.conic_section





    






            


        






            
            
      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        