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

equations = {
    #separable equations
    # 'dr/dt = - 4rt': 'r = ro exp(- 2t^2 )',
    # """2xyy' = 1 + y^2 when x = 2, y = 3""":"""y = sqrt(5x - 1)""",
    # """xyy' = 1 + y^2 when x = 2, y = 3""":"""y = (1/2) * sqrt(10x^2 - 4)""",
    # """2ydx = 3xdy when x = 2, y = 1""":"""y = (x/2)^(2/3)""",
    # """2ydx = 3xdy when x = - 2, y = 1""":"""y = (x/2)^(2/3)""",
    # """2ydx = 3xdy when x = 2, y = - 1""":"""y =  - (x/2)^(2/3)""",
    # """y = x exp(y - x^2) when x = 0, y = 0""":"""y = ln[2/(1 + exp(-x^2))]""",
    # """xy^2 dx + e^x dy = 0 when x approaches inf, y approaches 1/2""":"""y = [(exp(x))/(2exp(x) - x - 1)]""",
    """(1-x) y' = y^2""":"""y ln | c (1 - x) | = 1""",
    """sin(x) sin(y) dx + cos(x) cos(y) dy = 0""":"""sin(y) = c cos(x)""",
    """xy^3 dx + exp(x^2) dy = 0""":"""exp(-x^2) + y^(-2) = c""",
    """2y dx = 3x dy""":"""x^2 = cy^3""",
    # """my dx = nx dy""":"""x^m = cy^n""",
    """y' = xy^2""":"""y(x^2 + c) + 2 = 0""",
    """y exp(2x) dx = (4 + exp(2x)) dy""":"""c^2 y^2 = 4 + exp(2x)""",
    """xy dx - (x + 2) dy = 0""":"""exp(x) = cy(x + 2)^2""",
    """x^2 dx + y(x- 1) dy = 0""":"""(x + 1)^2 + y^2 + 2 ln |c (x - 1)| = 0""",
    """(xy + x) dx = (x^2 y^2 + x^2 + y^2 + 1) dy = 0""":"""ln(x^2 + 1) = y^2 - 2y + 4 ln|c(y + 1)|""",
    """x cos^2(y) dx + tan(y) dy = 0""":"""x^2 + tan^2(y) = c^2""",
    """x y^3 dx + (y + 1)exp(-x) dy = 0""":"""exp(x)(x  - 1) = 1/y + 1/(2y^2) + c""",
    """(1 - y) y' = x^2""":"""2x^3 + 3y^2 - 6y = c""",
    """x^2yy' = exp(y)""":"""x ( y + 1 ) = (1 + cx) exp(y)""",
    """tan^2(y) dy = sin^3(x) dx""":"""cos^3(x) - 3 cos(x) = 3 (tan(y) - y + c)""",
    """y' = cos^2(x) cos(y)""":"""4 ln|sec(y) + tan(y) |  = 2x + sin(2x) + c""",
    """y' = y sec(x)""":"""y = c (sec(x) + tan(x))""",
    """(exp(2x) + 4) y' = y""":"""y^8 (1 + 4 exp(-2x)) = c^2""",
    """(1 + ln(x)) dx + (1 + ln(y)) dy = 0""":"""x ln(x) + y ln (y) = c""",
    """y ln(x) ln(y) dx + dy = 0""":"""x ln(x) + ln | ln(y) | = x + c""",

    #exact equations
    """3 (3 x^2 + y^2) dx - 2xy dy = 0""":"""x^3 = c(9x^2 + y^2)""",
    """(x - 2y) dx + (2x + y) dy = 0""":"""ln(x^2 + y^2) + 4 arctan(y/x) = c""",
    """2(2x^2 + y^2) dx - xy dy = 0""":"""x^4 = c^2 (4x^2 + y^2)""",
    """xy dx - (x^2 + 3y^2) dy = 0""":"""x^2 = 6y^2 ln |y/c|""",
    """x^2 y' = 4x^2 + 7xy + 2y^2""":"""x^2(y + 2x) = c(y + x)""",
    """3xy dx + (x^2 + y^2) dy = 0""":"""x^2(y + 2x) = c(y + x)""",
    """(x - y)(4x + y) dx + x(5x - y)dy = 0""":"""x (y + x)^2 = c(y - 2x)""",
    """(x^2 + 2xy - 4y^2) dx - (x^2 - 8xy - 4y^2) dy = 0""":"""x^2 + 4y^2 = c(x + y )""",
    """x (x^2 + y^2)^2(ydx - xdy) + y^6 dy = 0""":"""(x^2 + y^2)^3 = 6y^6 ln |c/y|""",
    """(x^2 + y^2) dx + xy dy = 0""":"""x^2 ( x^2 + 2y^2) = c^4""",
    """xy dx - (x + 2y)^2 dy = 0""":"""y^3(x + y) = c exp(x/y)""",
    """[x csc(y/x) - y] dx + x dy = 0""":"""ln|x/c| = cos(y/x)""",
    """x dx + sin^2(y/x) [ydx - xdy] = 0""":"""4x ln|x/c| - 2y + x sin(2y/x) = 0""",
    """(x - y ln(y) + y ln(x)) dx + x(ln(y) - ln(x)) dy = 0""":"""(x - y) ln(x) + y ln(y) = cx + y""",
    """[x - y arctan(y/x) ]dx + x arctan(y/x) dy = 0""":"""2y arctan(y/x) = xln[c^2(x^2 + y^2)/x^4]""",
    """y^2 dy = x (x dy - ydx) exp(x/y)""":"""y ln | y/c | = (y - x)exp(x/y)""",
    """y dx = (x + sqrt(y^2 + x^2)) dy""":"""arcsin(x/y) = ln|y/c|""",
    """(3x^2 - 2xy + 3y^2) dx = 4xydy""":"""(y - x)(y + 3x)^3 = cx^3""",
    # """(x - y)dx + (3x + y) dy = 0, when x = 3, y = -2""":"""2(2x + 3y) + (x + y) ln (x + y) = 0""",
    # """(y - sqrt(x^2 + y^2)) dx - x dy = 0 when x = 0, y = 1""":"""x^2 = 4 - 4y""",
    # """(y + sqrt(x^2 + y^2)) dx - x dy = 0 when x = sqrt(3), y = 1""":"""x^2 = 2y + 1""",
    # """[x cos^2(y/x) - y] dx + xdy = 0 when x = 1, y = pi/4""":"""tan(y/x) = ln(e/x)""",
    # """(y^2 + 7xy + 16x^2) dx + x^2 dy = 0, when x = 1, y = 1""":"""x - y = 5(y + 4x) ln(x)""",
    # """y^2 dx + (x^2 + 3xy + 4y^2) dy = 0, when x = 2, y = 1""":"""4(2y + x)ln(y) = 2y - x""",
    # """xy dx + 2(x^2 + 2y^2) dy = 0, when x = 0, y = 1""":"""y^4 (3x^2 + 4y^2) = 4""",
    # """y(2x^2 - xy + y^2) dx - x^2 (2x - y) dy = 0, when  x = 1, y = 1/2""":"""y^2 ln(x) = 2y^2 + xy - x^2""",
    # """y(9x - 2y) dx - x(6x - y)dy = 0 when x =1, y = 1""":"""3x^3 - x^2 y - 2y^2 = 0""",
    # """y(x^2 + y^2) dx + x (3x^2 - 5y^2) dy = 0  when x = 2, y = 1""":"""2y^5 - 2x^2 y^3 = 3x = 0""",
    # """(16x + 5y) dx + (3x + y) dy = 0; the curve passes through the point (1, -3)""":"""y + 3x = (y + 4x) ln(y + 4x)""",
    # """(3x^2 - 2y^2) y' = 2xy when x = 0, y = -1""":"""x^2 = 2y^2(y + 1)""",

    #exact equations
    """(x + y)dx + (x - y) dy = 0""":"""x^2 + 2xy - y^2 = c""",
    """(6x + y^2) dx + y(2x - 3y) dy = 0""":"""3x^2 + xy^2 - y^3 = c""",
    """(2xy - 3x^2) dx + (x^2 + y) dy = 0""":"""x^2 y - x^3 + 0.5 y^2 = c""",
    """(y^2 - 2xy + 6x) dx - (x^2 - 2xy + 2) dy = 0""":"""xy^2 - x^2 y + 3x^2 - 2y = c""",
    """(2xy + y) dx = (x^2 - x) dy = 0""":"""y = cx(x - 1)^-3""",
    """(x - 2y) dx + 2(y - x)dy = 0""":"""x^2 + 2y^2 = 2xy + c""",
    """(2x - 3y) dx + (2y - 3x) dy = 0""":"""x^2 + y^2 = 3xy + c""",
    """(cos(2y) - 3x^2 y^2) dx + (cos(2y) - 2x sin(2y) - 2x^3 y) dy = 0""":"""0.5 sin(2y) + x cos(2y) - x^3 y^2 = c""",
    """(1 + y^2) dx + (x^2 y + y)dy = 0""":"""2 arctan(x) + ln(1 + y^2) = c""",
    """(1 + y^2 + xy^2) dx + (x^2 y + y + 2xy) dy = 0""":"""2x + y^2 ( 1 + x)^2 = c""",
    """(2xy - tan(y)) dx + (x^2 - x sec^2(y)) dy = 0""":"""x^2 y - x tan(y) = c""",
    """(cos(x) cos(y) - cot(x)) dx - (sin(x) sin(y)) dy = 0""":"""sin(x) cos(y) = ln|c sin(x)|""",
    """x(3xy - 4y^3 + 6)dx + (x^3 - 6x^2 y^2 - 1) dy = 0""":"""x^3 y - 2x^2 y^3 + 3x^2 - y = c""",
    """[2x + y cos(xy)] dx + x cos(xy) dy = 0""":"""x^2 + sin(xy) = c""",
    """2y dx + (y^2 + x^2) dy = 0""":"""y(3x^2 + y^2) = c""",
    """2y dx + (y^2 - x^2) dy = 0""":"""x^2 + y^2 = cy""",
    """(xy^2 + y - x) dx  + x (xy + 1) dy = 0""":"""x^2 y^2 + 2xy - x^2 = c""",

    #linear equations
    """(x^5 + 3y) dx - x dy = 0""":"""2y = x^5 + cx^3 """,
    """2 (2xy + 4y - 3) dx + (x + 2)^2 dy = 0""":"""y = 2(x + 2)^(-1) + c(x + 2)^(-4)""",
    """y' = x - 2y""":"""4y = 2x - 1 + c exp(-2x)""",
    """(y + 1)dx + (4x - y) dy = 0""":"""20x = 4y - 1 + c(y + 1)^(-4)""",
    """y' = x - 4xy""":"""4y = 1 + c exp(-2x^2)""",
    """y' = csc(x) + y cot(x)""":"""y = c sin(x) - cos(x)""",
    """y' = csc(x) - y cot(x)""":"""y sin(x) = x + c""",
    """(2xy + x^3 + x^4) dx - (1 + x^2) dy = 0""":"""y = (1 + x^2)(c + x - arctan(x))""",
    """y - cos^2(x) dx + cos(x) dy = 0""":"""y(sec(x) + tan(x)) = c + x - cos(x)""",
    """y' = x - 2y cot(2x)""":"""4ysin(2x) = c + sin(2x) - 2x cos(2x)""",
    """(y - x + xy cot(x)) dx + x dy = 0""":"""xy sin(x) = c + sin(x) - x cos(x)""",
    """x(x^2 + 1)y' + 2y = (x^2 + 1)^3""":"""x^2 y = 0.25 (x^2 + 1)^3 + c(x^2 + 1)""",
    """2y(y^2 - x) dy = dx""":"""x = y^2 - 1  + c exp(-y^2)""",
    """2y dx = (x^2 - 1)(dx - dy)""":"""(x - 1)y = (x + 1)(c + x - 2 ln|x +1|)""",
    """dx - (1 + 2x tan(y)) dy = 0""":"""2x cos^2(y) = y + c + sin(y) cos(y)""",
    """(1 + cos(x)) y' = sin(x)[sin(x) + sin(x)cos(x) - y]""":"""y = (1 + cos(x))(c + x - sin(x))""",
    """y' = 1 + 3ytan(x)""":"""3y cos^3(x) = c + 3 sin(x) - sin^3(x)""",

    #to be continued miscellaneous equations


}


equations_de2 = {
    #obtaining the general solution of a linear DE second order.
    """(D^2 + D) y = - cos(x)""":"""y = c1 + c2 exp(-x) + 0.5 cos(x) - 0.5 sin(x)""",
    """(D^2 - 6D + 9)y = exp(x)""":"""y = (c1 + c2x)exp(3x) + 0.25 exp(x)""",
    """(D^2 + 3D + 2)y = 12 x^2""":"""y = c1 e^(-x) + c2 e^(-2x) + 6x^2 - 18x + 21""",
    """(D^2 + 3D + 2)y = 1 + 3x + x^2""":"""y = c1 e^(-x) + c2 e^(-2x) + 0.5 x^2""",
    """(D^2 + 9) y = 5e^(x) - 162x """:"""y = c1 cos(3x) + c2 sin(3x) + 0.5e^x - 18x""",
    """(D^2 + 9) y = 5e^(x) - 162x^2""":"""y = c1 cos(3x) + c2 sin(3x) + 0.5e^x - 18x^2 + 4""",
    """y" - 3y' - 4y = 30e^x""":"""y = c1 e^(4x) + c2 e^(-x) - 5e^x""",
    """y" - 3y' - 4y = 30e(4x)""":"""y = (c1 + 6x)e^(4x) + c2 e^(-x)""",
    """(D^2 - 4)y = e^(2x) + 2""":"""y = c1 e^(-2x) + (c2 + 0.25 x)e^(2x) - 0.5""",
    """(D^2 - D - 2)y = 6x + 6e^(-x)""":"""y = c1 e^(-x) + c2 e^(2x) - 3x + 3/2 - 2xe^(-x)""",
    """y" - 4y' + 3y = 20 cos(x)""":"""y = c1 e^(x) + c2 e^(3x) + 2 cos(x) - 4 sin(x)""",
    """y" - 4y' + 3y = 2 cos(x) + 4 sin(x)""":"""y = c1 e^(x) + c2 e^(3x) + cos(x)""",
    """y" + 2y' + y = 7 + 75 sin(2x)""":"""y = e^(-x) (c1 + c2 x) + 7 - 12 cos(2x) - 9 sin(2x)""",
    """(D^2 + 4D + 5)y = 50 x + 13 e^(3x)""":"""y = e^(-2x) (c1 cos(x) + c2 sin(x)) + 10x - 8 + 0.5 e^(3x)""",
    """(D^2 + 1)y = cos(x)""":"""y = c1 cos(x) + c2 sin(x) + 0.5 x sin(x)""",
    """(D^2 - 4D - 4) y = e^(2x)""":"""y = e^(2x) (c1 + c2 x + 0.5 x^2)""",
    """(D^2 - 1)y = 8x e^x """:"""y = c1 e^(-x) + e^x (c2 - 2x + 2x^2)""",
    """(D^3 - D)y = x""":"""y = c1 + c2 e^(x) + c3 e^(-x) - 0.5x^2""",
    """(D^3 - D^2 + D - 1)y = 4 sin(x)""":"""y = c1 e^x + (c2 + x) cos(x) + (c3 - x)sin(x)""",
    """(D^3 + D^2 - 4D - 4) y = 3e^(-x) - 4x - 6""":"""y = c1 e^(2x) + c2e(-2x) + (c3 - x)e^(-x) + x + 0.5""",
    """(D^4 - 1)y = e^(-x)""":"""y = c1 e^x + (c2 - 0.25 x) e^(-x) + c3 cos(x) + c4 sin(x)""",
    """(D^2 - 1)y = 10 sin^2(x)""":"""y = c1 e^x + c2 e^(-x) - 5 + cos(2x)""",
    """(D^2 + 1)y = 12 cos^2(x)""":"""y = c1 cos(x) + c2 sin(x) + 6 - 2cos(2x)""",
    """(D^2 + 4)y = 4 sin^2(x)""":"""y = c1 cos(2x) + c2 sin(2x) + 0.5(1 - x sin(2x))"""
}




class DE_1():
    def __init__(self):
        key = random.choice(list(equations.keys()))

        self.question = f"""Solve the solution to the differential equation {key}"""
        self.answer = equations[key]

class DE_2():
    def __init__(self):
        key = random.choice(list(equations_de2.keys()))

        self.question = f"""Solve the solution to the differential equation {key}"""
        self.answer = equations_de2[key]


































































































        




























































