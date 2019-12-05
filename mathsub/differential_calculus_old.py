import random_handler as ran
import numpy_handler as num
import sympy as sym
from sympy import init_printing
from sympy import div
import math
import random
import algebra

x, y = sym.symbols('x y', real = True)

init_printing(use_unicode=True)

class limits_rational_poly_poly:
    def __init__(self, random_range = 10):
        approach = ran.c(10)
        numerator_obj = algebra.polynomial(random_range)
        denominator_obj = algebra.polynomial(random_range)
        rational_expression = numerator_obj.expression/denominator_obj.expression
        #expression_0 = -9*x/(-8*x**2 + 7*x - 3)
        expression_limit = sym.Limit(rational_expression, x, approach)
    
        expression_done = expression_limit.doit()
        
        
        self.limit = expression_done
        self.expression = expression_limit
        
class derivative_rational_poly_poly:
    def __init__(self, random_range = 10):

        numerator_obj = algebra.polynomial(random_range)
        denominator_obj = algebra.polynomial(random_range)
        rational_expression = numerator_obj.expression/denominator_obj.expression
        #expression_0 = -9*x/(-8*x**2 + 7*x - 3)
        expression_deriv = sym.Derivative(rational_expression, x)
    
        expression_done = expression_deriv.doit()
        
        
        self.derivative = expression_done
        self.expression = expression_deriv
        
class derivative_square_root_poly:
    def __init__(self, random_range = 10):

        poly_obj = algebra.polynomial(random_range)
        root_expression = (poly_obj.expression)**(sym.Rational(1,random.randint(2,3)))
        #expression_0 = -9*x/(-8*x**2 + 7*x - 3)
        expression_deriv = sym.Derivative(root_expression, x)
    
        expression_done = expression_deriv.doit()
        
        
        self.derivative = expression_done
        self.expression = expression_deriv
        
#testprint = limits_rational()
#print(testprint.expression)
#print(testprint.doit)

