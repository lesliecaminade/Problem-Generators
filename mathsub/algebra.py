from generator import random_handler as ran
import sympy as sym
import math
import random
from generator import constants_conversions as c
from num2words import num2words
from mathsub import algebra_engine as ae

x, y, z, t = sym.symbols('x y z t', real = True)
a, b, c = sym.symbols('a b c', real = True)

class algebra_1:
    def __init__(self):
        #univariate degree
        polynomial = ae.Polynomial()
        polynomial.init_random(random.randint(2,6))
        self.question = f"""Determine the degree of the polynomial 
{sym.pretty(polynomial.expression.as_expr())}
"""

        degree = polynomial.degree()

        self.answer = f"""{degree}"""

class algebra_2:
    def __init__(self):
        #multivariate degree
        polynomial = ae.Polynomial()
        polynomial.init_random(random.randint(2,5), 2)
        self.question = f"""Determine the degree of the multivariate polynomial 
{sym.pretty(polynomial.expression.as_expr())}
"""
        degree = polynomial.degree()
        self.answer = f"""{degree}"""

class algebra_3:
    def __init__(self):
        #computation of the discriminant
        quadratic = ae.Quadratic()
        quadratic.init_random()
        #equation = sym.Eq(quadratic.expression, 0)

        self.question = f"""Compute the discriminant of the quadratic equation
{sym.pretty(quadratic.expression.as_expr())}
"""

        self.answer = f"""{quadratic.discriminant()}"""

class algebra_4:
    def __init__(self):
        #equal roots discriminant
        tryagain = True
        while tryagain:
            try:
                equal_roots = 0
                while equal_roots == 0:
                    equal_roots = random.randint(-9, 9)

                leading = ae.random_coeff()
                quadratic = sym.Poly((leading*x - equal_roots) * (leading*x - equal_roots))

                equation = sym.Eq(quadratic, 0)

                if not(quadratic.discriminant() == 0):
                    print('algebra_4 error')

                coefficients = quadratic.all_coeffs()
                A = coefficients[0]
                B = coefficients[1]
                C = coefficients[2]

                tryagain = False
            except:
                tryagain = True

        self.question = f"""Given that the polynomial A x^2 + {B} x + {C} = 0 has equal roots, determine the value of A."""

        self.answer = f"""{A}"""

class algebra_5:
    #sum of the roots of a polynomial
    def __init__(self):
        polynomial = ae.Polynomial()
        polynomial.init_random(random.randint(3,9))
        #equation = sym.Eq(polynomial.expression, 0)

        self.question = f"""Determine the sum of the roots of the polynomial
{sym.pretty(polynomial.expression.as_expr())}
"""

        sum_of_the_roots = polynomial.sum_of_the_roots()

        self.answer = f"""{sum_of_the_roots}"""

class algebra_6:
    #product of the roots of a polynomial
    def __init__(self):
        polynomial = ae.Polynomial()
        polynomial.init_random(random.randint(3,9))
        #equation = sym.Eq(polynomial.expression, 0)

        self.question = f"""Determine the product of the roots of the polynomial
{sym.pretty(polynomial.expression.as_expr())}
"""
        product_of_the_roots = polynomial.product_of_the_roots()

        self.answer = f"""{product_of_the_roots}"""

class algebra_7:
    def __init__(self):
        #remainder theorem (remainder)
        polynomial = ae.Polynomial()
        polynomial.init_random(random.randint(3,9))

        divisor = ae.Polynomial()
        divisor.init_random(2) #linear divisor

        result = ['quotient', 'remainder']
        result = sym.div(polynomial.expression, divisor.expression)
        quotient = result[0]
        remainder = result[1]

        self.question  = f"""Determine the remainder of 
{sym.pretty(polynomial.expression.as_expr())}
when divided by 
{sym.pretty(divisor.expression.as_expr())}"""

        self.answer = f"""{remainder.as_expr()}"""


class algebra_8:
    def __init__(self):
        #remainder theorem (quotient)
        polynomial = ae.Polynomial()
        polynomial.init_random(random.randint(3,9))

        divisor = ae.Polynomial()
        divisor.init_random(2) #linear divisor

        result = ['quotient', 'remainder']
        result = sym.div(polynomial.expression, divisor.expression)
        quotient = result[0]
        remainder = result[1]

        self.question  = f"""Determine the depressed equation of 
{sym.pretty(polynomial.expression.as_expr())}
when divided by 
{sym.pretty(divisor.expression.as_expr())}"""

        self.answer = f"""{sym.pretty(quotient.as_expr())}"""


class algebra_9:
    def __init__(self):
        #evaluating functions
        polynomial = ae.Polynomial()
        polynomial.init_random(random.randint(3,5))

        input_num = ae.random_coeff()

        self.question = f"""If f(x) = ...
{sym.pretty(polynomial.expression.as_expr())}
what is the value of 
f({input_num})?"""

        output_num = polynomial.expression.subs(x, input_num)

        self.answer = f"""{output_num}"""

class algebra_10:
    def __init__(self):
        #evaluating discrete functions
        function_f = ae.DiscreteFunction()
        function_g = ae.DiscreteFunction()
        function_f.init_random(1,4,1)
        function_g.init_random(1,4,1)

        input_value = random.randint(1,4)

        self.question = f"""Two functions f and g satisfy the following relationships
f(1) = {function_f.substitute(1)}
f(2) = {function_f.substitute(2)}
f(3) = {function_f.substitute(3)}
f(4) = {function_f.substitute(4)}
g(1) = {function_g.substitute(1)}
g(2) = {function_g.substitute(2)}
g(3) = {function_g.substitute(3)}
g(4) = {function_g.substitute(4)}
What is the value of (f o g) ({input_value})?"""

        output_value = function_f.substitute(function_g.substitute(input_value))

        self.answer = f"""{output_value}"""

class algebra_11:
    def __init__(self):
        #evaluating functions reverse
        quadratic = ae.Quadratic()
        A = ae.random_coeff()
        B = ae.random_coeff()
        C = ae.random_coeff()

        quadratic.init_coeff(A, B, C)

        quadratic2 = ae.Quadratic()
        quadratic2.init_coeff(a, B, C)

        input_value = ae.random_coeff()

        output_value = quadratic.substitute( input_value)

        self.question = f"""If f(x) = ...
{sym.pretty(quadratic2.expression.as_expr())}
What is the value of a satisfying
f({input_value}) = {output_value}?"""

        self.answer = f"""{A}"""

class algebra_12:
    def __init__(self):
        #function arithmetic 1
        f_ = ae.Quadratic()
        g_ = ae.Quadratic()

        f_.init_random()
        g_.init_random()

        input_value_1 = ae.random_coeff()
        input_value_2 = ae.random_coeff()

        self.question = f"""Consider the functions f(x) = ...
{sym.pretty(f_.expression.as_expr())}
and g(x) = ...
{sym.pretty(g_.expression.as_expr())}
What is the value of f({input_value_1}) * g({input_value_2})?"""

        output_value = f_.substitute( input_value_1) * g_.substitute( input_value_2)

        self.answer = f"""{output_value}"""

class algebra_13:
    def __init__(self):
        #function arithmetic 2
        f_ = ae.Polynomial()
        g_ = ae.Polynomial()
        f_.init_random()
        g_.init_random()

        h_ = f_.expression + g_.expression
        k_ = f_.expression - g_.expression

        input_value_1 = ae.random_coeff()
        input_value_2 = ae.random_coeff()

        self.question = f"""Given the two functions f(x) = ...
{sym.pretty(f_.expression.as_expr())}
and g(x) = ...
{sym.pretty(g_.expression.as_expr())}
If h(x) = f(x) + g(x) and k(x) = f(x) - g(x)
What is the value of h({input_value_1}) * k({input_value_2})?"""

        output_value = h_.subs(x, input_value_1) * k_.subs(x, input_value_2)

        self.answer = f"""{output_value}"""

class algebra_14:
    def __init__(self):
        #function arithmetic reverse
        tryagain = True
        while tryagain:
            f_ = ae.Polynomial()
            g_ = ae.Polynomial()
            f_.init_random()
            g_.init_random()

            h_ = f_.expression + g_.expression
            try:
                k_ = g_.expression / f_.expression
                tryagain = False
            except:
                tryagain = True

        input_value_1 = ae.random_coeff()

        output_value = h_.subs(x, input_value_1) - k_.subs(x, input_value_1)

        self.question = f"""Consider the functions f(x) = ...
{sym.pretty(f_.expression.as_expr())}
and g(x) = ...
{sym.pretty(g_.expression.as_expr())}
If h(x) = f(x) + g(x) and k(x) = g(x) / f(x), what is the value of x satisfying
h(x) - k(x) = {output_value}?"""

        self.answer = f"""{input_value_1}"""

class algebra_15:
    def __init__(self):
        FORMS = 2
        #composition of functions
        f_ = ae.Polynomial()
        g_ = ae.Polynomial()
        f_.init_random()
        g_.init_random()

        input_value = ae.random_coeff()

        form = random.randint(1,FORMS)

        statement = ''

        if form == 1:
            statement = f"""g(f({input_value}))"""

        if form == 2:
            statement = f"""( g o f )({input_value})"""

        self.question = f"""Given the functions f(x) = ...
{sym.pretty(f_.expression.as_expr())}
and g(x) = ...
{sym.pretty(g_.expression.as_expr())}
Find the value of {statement}."""

        output_value = g_.substitute(f_.substitute(input_value))

        self.answer = f"""{output_value.as_expr()}"""

class algebra_16:
    def __init__(self):
        #composition of a composition of a composition
        f_ = ae.Quadratic()
        f_.init_random()

        input_value = random.randint(-2,2)
        output_value = input_value
        repetitions = random.randint(2,4)

        for i in range(repetitions):
            output_value = f_.substitute(output_value)

        statement = ''
        for i in range(repetitions):
            statement = statement + 'f(f(' 

        suffix = ''
        for i in range(repetitions):
            suffix = suffix + '))'

        self.question = f"""Let f be a function such that ( f o f )(x) = ...
{sym.pretty(f_.expression.as_expr())}
What is the value of {statement}{input_value}{suffix}?"""

        self.answer = f"""{output_value}"""

class algebra_17:
    def __init__(self):
        #composition of a function piecewise
        f_ = ae.Linear()
        g_ = ae.Piecewise()

        f_.init_random()
        g_.init_random(2)

        input_value_1 = ae.random_coeff()
        input_value_2 = ae.random_coeff()

        self.question = f"""Consider the two functions f(x) = ...
{sym.pretty(f_.expression.as_expr())}
and g(x) = ...
{sym.pretty(g_.expression)}
What is the value of (f o g)({input_value_1}) + (g o f)({input_value_2})?"""

        output_value = f_.substitute(g_.substitute(input_value_1)) + g_.substitute(f_.substitute(input_value_2))

        self.answer = f"""{output_value}"""

class algebra_18:
    def __init__(self):
        #composition of functions internal 
        f_ = ae.Quadratic()
        g_ = ae.Linear()

        f_.init_random()
        g_.init_random()

        input_value = ae.random_coeff()

        semi_input_value = g_.substitute(input_value)

        output_value = f_.substitute(semi_input_value)

        self.question = f"""f : R -> R is a function satisfying f({g_.expression.as_expr()}) = {f_.expression.as_expr()}. What is the value of f({semi_input_value})?"""

        self.answer = f"""{output_value}"""

class algebra_19:
    def __init__(self):
        #inverse functions
        tryagain = True
        while tryagain:
            try:
                f_ = ae.Linear()
                f_.init_random()

                g_ = f_.inverse()

                input_value_1 = ae.random_coeff()
                input_value_2 = ae.random_coeff()
                tryagain = False
            except:
                tryagain = True

        self.question = f"""Let f(x) = ...
{sym.pretty(f_.expression.as_expr())}
and let g(x) = f-1(x)
what is the value of g({input_value_1}) + g-1({input_value_2})?"""

        output_value = g_.substitute(input_value_1) + f_.substitute(input_value_2)

        self.answer = f"""{output_value}"""

class algebra_20:
    def __init__(self):
        #inverse functions
        f_ = ae.Linear()
        f_.init_random()

        g_ = f_.inverse()

        input_value = ae.random_coeff()
        output_value_1 = g_.substitute(input_value)

        output_value_2 = f_.substitute(f_.substitute(output_value_1))

        self.question = f"""If f^-1({input_value}) = {output_value_1} and (f o f)({output_value_1}) = {output_value_2} for f(x) = ax + b, what is a + b?"""

        coefficients = f_.coefficients()
        A = coefficients[0]
        B = coefficients[1]

        self.answer = f"""{A + B}"""

class algebra_21:
    def __init__(self):
        #symbolic operators
        tryagain = True
        while tryagain:
            try:
                k = sym.symbols('k', real = True)
                k_ = ae.Polynomial()
                k_.init_expression(x**ae.random_power() - (x - ae.random_coeff())**ae.random_power())



                input_value = -1
                while input_value < 0:
                    input_value = ae.random_coeff()



                self.question = f"""For positive integer k, let dot_k_dot = {k_.expression.as_expr().subs(x, k)}, what is the value of dot_{input_value}_dot?"""

                output_value = k_.substitute(input_value)

                self.answer= f"""{output_value}"""
                tryagain = False
            except:
                tryagain = True

class algebra_22:
    def __init__(self):
        #symbolic operators 2
        m, n = sym.symbols('m n', real = True)

        expression = (m/n)**-1 - (n/m)**-1

        input_value_1 = ae.random_coeff()
        input_value_2 = ae.random_coeff()

        output_value = expression.subs(m, input_value_1).subs(n, input_value_2)

        self.question =f"""For positive integers m and n, let m_nabla_n be defined as 
{expression}
What is the value of {input_value_1}_nabla_{input_value_2}?"""

        self.answer = f"""{output_value}"""

class algebra_23:
    def __init__(self):
        #symbolic operators 3
        m, k, n = sym.symbols('m k n', real = True)

        input_m = ae.random_coeff()
        input_n = ae.random_coeff()
        input_k = ae.random_coeff()

        expression = k + m/n

        self.question = f"""For positive integers m, k^caret, n, let m k^caret n be defined as m k^caret n = k m/n where k m/n is a mixed fraction. What is the value of {input_m} {input_k}^caret {input_n} + {input_n} {input_k}^caret {input_m}?"""

        output_value_1 = expression.subs(m, input_m).subs(k, input_k).subs(n, input_n)

        output_value_2 = expression.subs(m, input_n).subs(k, input_k).subs(n, input_m)

        output_value = output_value_1 + output_value_2

        self.answer = f"""{output_value}"""

class algebra_24:
    def __init__(self):
        #inequalities quadratic
        q_ = ae.Quadratic()
        q_.init_random()

        i_ = ae.Inequality()
        i_.init_expression_random_inequality(q_.expression.as_expr(), ae.random_coeff())

        solution = i_.solve()

        self.question = f"""Find the range of x that satisfies the inequality {i_.expression}"""

        self.answer = f"""{solution}"""

class algebra_25:
    def __init__(self):
        #inequalities quadratic reverse

        q_ = ae.Quadratic()
        q_.init_roots(ae.random_coeff(), ae.random_coeff())

        i_ = ae.Inequality()
        i_.init_expression_random_inequality(q_.expression.as_expr(), ae.random_coeff())

        solution = i_.solve()

        self.question = f"""What is the quadratic inequality the solution of which is {solution}?"""

        self.answer = f"""{i_.expression}"""

class algebra_26:
    def __init__(self):
        #inequalities involving rationals

        n_ = ae.Quadratic()
        n_.init_random()

        d_ = ae.Quadratic()
        d_.init_random()

        i_ = ae.Inequality()
        i_.init_expression_random_inequality(n_.expression/d_.expression, ae.random_coeff())

        self.question = f"""Find the range of x that satisfies the inequality {i_.expression}"""

        solution = i_.solve()

        self.answer = f"""{solution}"""

class algebra_27:
    def __init__(self):
        #inequalities involving absolute values

        e_ = ae.Linear()
        e_.init_random()

        i_ = ae.Inequality()
        i_.init_expression_random_inequality(sym.Abs(e_.expression), ae.random_coeff())

        self.question = f"""Find the range of x that satisfies the inequality {i_.expression}"""

        self.answer = f"""{i_.solve()}"""


class algebra_28:
    def __init__(self):
        #partial fraction decomposition, distinct factors
        n_ = ae.Linear()
        n_.init_random()
        d_ = ae.Quadratic()
        d_.init_roots(ae.random_coeff(), ae.random_coeff())

        output = sym.apart(n_.expression/d_.expression)

        self.question = f"""Determine the partial fraction decomposition of 
{sym.pretty(n_.expression/d_.expression)}
."""

        self.answer = f"""{sym.pretty(output)}"""

class algebra_29:
    def __init__(self):
        #partial fraction decomposition, repeated factors
        n_ = ae.Quadratic()
        n_.init_random()
        d_ = ae.Polynomial()
        repeated_root = ae.random_coeff()
        d_.init_roots(ae.random_coeff(), repeated_root, repeated_root)

        output = sym.apart(n_.expression/d_.expression)

        self.question = f"""Determine the partial fraction decomposition of 
{sym.pretty(n_.expression/d_.expression)}
."""

        self.answer = f"""{sym.pretty(output)}"""

class algebra_30:
    def __init__(self):
        #partial fraction, irreducible factors
        n_ = ae.Linear()
        n_.init_random()

        d_ = ae.Polynomial()

        pos = -1
        while pos < 0:
            pos = ae.random_coeff()

        d_.init_expression((x**2 + pos) * (x - ae.random_coeff()))

        output = sym.apart(n_.expression/d_.expression)

        self.question = f"""Determine the partial fraction decomposition of 
{sym.pretty(n_.expression/d_.expression)}
."""

        self.answer = f"""{sym.pretty(output)}"""

class algebra_31:
    def __init__(self):
        #partial fraction, irreducible factors, repeated
        n_ = ae.Linear()
        n_.init_random()

        d_ = ae.Polynomial()

        pos = -1
        while pos < 0:
            pos = ae.random_coeff()

        d_.init_expression((x**2 + pos)**2 * (x - ae.random_coeff()))

        output = sym.apart(n_.expression/d_.expression)

        self.question = f"""Determine the partial fraction decomposition of 
{sym.pretty(n_.expression/d_.expression)}
."""

        self.answer = f"""{sym.pretty(output)}"""




























































