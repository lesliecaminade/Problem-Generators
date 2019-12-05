from generator import random_handler as ran
import sympy
import math
import random
from generator import constants_conversions as c
from mathsub import algebra_engine as ae
import num2words

x, y, z, t = sympy.symbols('x y z t', real = True)

SET_MAX = 50
SET_MIN = 0

COE_MAX = 10
POW_MAX = 3
BINOMIAL_POW_MIN = 3
BINOMIAL_POW_MAX = 10
            
def combination(n, r):
    combinations = math.factorial(n) / ( math.factorial(n - r) * math.factorial(r))
    return int(combinations)

def permutation(n, r):
    permutations = math.factorial(n) / math.factorial(n - r)
    return int(permutations)

def random_size():
    return random.randint(SET_MIN, SET_MAX)

def coe():
    return random.randint(-COE_MAX, COE_MAX)

def pow():
    return random.randint(-POW_MAX, POW_MAX)

def bpow():
    return random.randint(BINOMIAL_POW_MIN, BINOMIAL_POW_MAX)

def random_monomial():
    monomials =[ 
    coe() * x**pow(),
    coe() * y**pow(),
    coe() * x**pow() * y**pow()]
    return random.choice(monomials)

class Binomial_expansion():
    def __init__(self):
        self.A = random_monomial()
        self.B = random_monomial()
        self.N = bpow()
        self.factored = (self.A + self.B)**self.N
        self.expanded = sympy.expand(self.factored)
        self.number_of_terms = self.N + 1

        terms = []
        for i in range(self.number_of_terms):
            term = combination(self.N, i) * (self.A)**(self.N - i) * self.B**i
            terms.append(term)
        self.terms = terms

    def nth_term(self):
        term = random.randint(1, len(self.terms))
        return [self.terms[term - 1], term]

    def nth_coefficient(self, term):
        return self.terms[term + 1].subs(x, 1).subs(y, 1)

    def sum_of_the_coefficients(self, **kwargs):
        return self.expanded.subs(x, 1).subs(y, 1)















































