import randomizer
import math
import random
import sympy as sp
import stringHandling

from common_names import *
from sympy import *
from sympy.solvers.inequalities import solve_poly_inequality

#symbols for sympy
a, b, c, d, e, x, y, z = symbols('a b c d e x y z', real = True)
n = symbols('n', real = True)



class infiniteGeometricSeriesClass:

    def __init__(self):
        #try:
        
        coefficients = []
        constants = []
        
 
        form = random.randint(1,3)
        first_4_terms = []
        next_3_terms = []
        
        for i in range(0,20):
            
            coefficients.append(round(random.randint(-9,9),2)) 
            constants.append(round(random.randint(-50,50),2))
        
        if form == 1:
        
            ratio_greater_than_1 = random.randint(0,1)
            numerator = random.randint(1,9)
            denominator = random.randint(10,20)
            func1 = coefficients[0] * Pow(Rational(numerator,denominator),n-1)
            sum_of_infinite_terms = func1.subs(n,1)/(1-Rational(numerator,denominator))
            
            problem = """Evaluate the series:
∑ ({a:g} • ({b:g}/{c:g})^(n-1), n = 1 to ∞)""".format(a=coefficients[0],b =numerator,c=denominator)
            
            soln = sum_of_infinite_terms
            
        if form == 2:
            ratio_greater_than_1 = random.randint(0,1)
            numerator = random.randint(1,9)
            denominator = random.randint(10,20)
            func1 = coefficients[0] * Pow(Rational(numerator,denominator),n-1)
            sum_of_infinite_terms = func1.subs(n,1)/(1-Rational(numerator,denominator))
            
            show_as = Add(func1.subs(n,1),func1.subs(n,2),func1.subs(n,3),func1.subs(n,4),evaluate = False)
            show_as = str(show_as) + '  ...'

            
            problem = """Evaluate the series:
{a:s}""".format(a = show_as)
            
            soln = sum_of_infinite_terms  

        if form == 3:
            first_term = random.randint(1,9)
            sum_of_infinite_terms = random.randint(1,20)
            while sum_of_infinite_terms <= first_term:
                sum_of_infinite_terms = random.randint(1,20)
            
            common_ratio = solveset(Eq(sum_of_infinite_terms,first_term/(1-x)),x).args[0]
            
            problem = """Determine the common ratio of the series:
a_1 = {a:g} , S = {b:g}""".format(a=first_term,b=sum_of_infinite_terms)
            soln = common_ratio
            
            
        self.question = problem
        self.soln = soln
       


print('INFINITE GEOMETRIC SERIES')
print()


 
for i in range (1,10):
    A = infiniteGeometricSeriesClass()
    print("P: " + str(stringHandling.cleanAst(A.question))) 
    print("""S1 {a:s}""".format(a=stringHandling.cleanAst(stringHandling.removeBrackets(str(A.soln)))))

    print()




stay = True
while stay:
    command = input()
    if command == 'exit':
        stay = False
