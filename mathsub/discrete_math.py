from generator import random_handler as ran
import sympy as sym
import math
import random
from generator import constants_conversions as c
from mathsub import discrete_math_engine as de
from num2words import num2words
from mathsub import algebra_engine as ae

x, y, z, t = sym.symbols('x y z t', real = True)#generic variables
            
class binomial_1:
    def __init__(self):
        #binomial expansion x and y
        b_ = de.Binomial()
        b_.init_random()

        self.question = f"""Determine the binomial expansion of 
{sym.pretty(b_.compressed())}"""

        self.answer = f"""{b_.expand()}"""

class binomial_2:
    def __init__(self):
        #binomial expansion of pure x
        b_ = de.Binomial()
        b_.init_random(True)

        self.question = f"""Determine the binomial expansion of 
{sym.pretty(b_.compressed())}"""

        self.answer = f"""{b_.expand()}"""

class binomial_3:
    def __init__(self):
        #nth term
        b_ = de.Binomial()
        b_.init_random()

        nth = random.randint(1, b_.N + 1)
        self.question = f"""Determine the {num2words(nth, 'ordinal')} term of the expansion of
{sym.pretty(b_.compressed())}"""

        self.answer = f"""{sym.pretty(b_.nth_term(nth))}"""

class binomial_4:
    def __init__(self):
        tryagain = True

        while tryagain:
            try:
                #nth coefficient
                b_ = de.Binomial()
                b_.init_random()

                nth = random.randint(1, b_.N + 1)
                self.question = f"""Determine the coefficient of the {num2words(nth, 'ordinal')} term of the expansion of
        {sym.pretty(b_.compressed())}"""

                self.answer = f"""{sym.pretty(b_.nth_coefficient(nth))}"""
                tryagain = False
            except:
                tryagain = True

class binomial_5:
    def __init__(self):
        #term involving x^number or 
        b_ = de.Binomial()
        b_.init_random()


        self.question = f"""Determine the term involving x^n or y^n in the expansion of
{sym.pretty(b_.compressed())}"""

        self.answer = f"""{b_.expand()} (Note: manually search for answer - code still in development)"""

class binomial_6:
    def __init__(self):
        #term involving x^number x - only
        b_ = de.Binomial()
        b_.init_random(True)


        self.question = f"""Determine the term involving x^n in the expansion of
{sym.pretty(b_.compressed())}"""

        self.answer = f"""{b_.expand()} (Note: manually search for answer - code still in development)"""

class binomial_7:
    def __init__(self):
        #term independent of x
        b_ = de.Binomial()
        b_.init_random(True)

        self.question = f"""Determine the term independent of x in the expansion of
{sym.pretty(b_.compressed())}"""

        self.answer = f"""{b_.expand()} (Note: manually search for the constant term - code still in development)"""

class binomial_8:
    def __init__(self):
        #sum of the coefficients
        b_ = de.Binomial()
        b_.init_random()

        self.question = f"""Determine the sum of the coefficients in the expansion of
{sym.pretty(b_.compressed())}"""

        self.answer = f"""{b_.sum_of_the_coefficients()}"""















 































































