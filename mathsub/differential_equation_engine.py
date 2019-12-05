from generator import random_handler as ran
import sympy as sym
import math
import random
from generator import constants_conversions as c
from mathsub import algebra_engine
from mathsub import analytic_geometry_engine
from mathsub import differential_calculus_engine
from mathsub import integral_calculus_engine

import wolframalpha
WOLFRAM_NAME = 'ProblemGenerator'
WOLFRAM_APPID = 'VV7LX5-5V58TH8KJX'
client = wolframalpha.Client(WOLFRAM_APPID)

MAX_COE = 9

COMMON_FACTOR_MAX = 5
COMMON_FACTOR_POWER_MAX = 2

COEFFICIENTS = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
COEFFICIENT_WEIGHTS = [0.01875, 0.01875, 0.01875, 0.01875, 0.4, 0.05, 0.4, 0.01875, 0.01875, 0.01875, 0.01875]
million_samples = random.choices(COEFFICIENTS, COEFFICIENT_WEIGHTS, k =10000)


# print(million_samples)

x, y, z, t = sym.symbols('x y z t', real = True) 
#these are the sympy symbols that can be used
def random_coeff():
    return random.choice(million_samples)

def exact_generator(M):
    #takes a value of M
    #and computes the value of N such that 
    #partial M w/y = partial N w/x
    dMy = sym.diff(M, y)
    N = sym.integrate(dMy, x)
    N = N + random.randint(-MAX_COE, MAX_COE)

    return N

def trigonometric_generator():
    #returns any trigonometric function
    return random_coeff() * random.choice([sym.sin(x), sym.cos(x)])

def homogeneous_generator():
    #finds a value of M and finds the value of N such that the homogenity of M and N are equal
    def common_factor():
        variable = random.choice([x, y])
        return random_coeff() * variable **random.randint(0, COMMON_FACTOR_POWER_MAX)

    internals = [random_coeff() * x**2 + random_coeff() * y**2, 
    random_coeff() * x + random_coeff() * y,
    random_coeff() * x**2 + random_coeff() * x * y + random_coeff() * y**2,
    (random_coeff() * x + random_coeff() * y) * (random_coeff() * x + random_coeff() * y)]


    return random.choice(internals)

class Separable():
    def __init__(self):
        pass

    def init_random(self):
        #create M(x) and N(y)

        M = algebra_engine.ShortPolynomial().init_random()
        N = algebra_engine.ShortPolynomial().init_random()
        N.subs(x, y)

        string_query = f"""solve ({M})dx + ({N})dy = 0"""
        wolfram = client.query(string_query)

        results = next(wolfram.results).text

        self.de = f"""({M})dx + ({N})dy = 0"""
        self.results = results


class Exact():
    def __init__(self):
        pass

    def init_random(self):
        not_exact = True

        while not_exact:
            #create M(x,y) and N(x,y)
            M = algebra_engine.Bivariable().init_random(terms = 3)
            print(M)
            N = exact_generator(M)
            print(N)
            #test for exactness

            dMy = sym.diff(M, y)
            dNx = sym.diff(N, x)

            print(dMy)
            print(dNx)

            if dMy == dNx and not (M==N) :
                not_exact = False


        string_query = f"""solve ({M})dx + ({N})dy = 0"""
        wolfram = client.query(string_query)

        results = next(wolfram.results).text

        self.de = f"""({M})dx + ({N})dy = 0"""
        self.results = results

class Homogeneous():
    def __init__(self):
        pass

    def init_random(self):
        not_homo = True

        while not_homo:
            #create M(x,y) and N(x,y)
            M = homogeneous_generator()
            print(M)
            N = homogeneous_generator()
            print(N)


            #test for homogenity
            orderM = sym.homogeneous_order(M, x, y)
            orderN = sym.homogeneous_order(N, x, y)
            print('order M: ', orderM )
            print('order N: ', orderN )

            if orderM == orderN and not (orderM == None) and not (orderN == None):
                not_homo = False


        string_query = f"""solve ({M})dx + ({N})dy = 0"""
        wolfram = client.query(string_query)

        results = next(wolfram.results).text

        self.de = f"""({M})dx + ({N})dy = 0"""
        self.results = results

class Linear():
    def __init__(self):
        pass

    def init_random(self):

        #pick a P(x) and Q(x), which can be any function of x

        p_of_x = random_coeff() * x**random.choice([-2, -1, 1, 2])
        q_of_x = random_coeff() * x**random.choice([-2, -1, 1, 2])



        #construct the DE

        string_query = f"""solve dy/dx + ({p_of_x}) * y = {q_of_x}"""
        wolfram = client.query(string_query)

        results = next(wolfram.results).text

        self.de = f"""dy/dx + ({p_of_x}) y = {q_of_x}"""
        self.results = results









































































































        




























































