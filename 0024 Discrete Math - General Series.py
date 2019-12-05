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



class generalProgressionClass:

    def __init__(self):
        #try:
        
        coefficients = []
        constants = []
 
        form = random.randint(1,2)
        first_4_terms = []
        next_3_terms = []
        
        for i in range(0,20):
            coefficients.append(round(random.randint(-9,9),2)) 
            constants.append(round(random.randint(-50,50),2))

        if form == 1:  #basic arithmetic progression  
            func1 = constants[0] + coefficients[0]*x #explicit formula
            for i in range(1,5):
                first_4_terms.append(round(float(func1.subs(x,i))),2)
            for i in range (5,8):
                next_3_terms.append(round(float(func1.subs(x,i))),2)

            soln = next_3_terms
            if coefficients[0] >= 0:
                sign = '+'
            else:
                sign = ''
            soln2 = """a_n = {a:g} {s:s}{b:g}n""".format(a=constants[0],b=coefficients[0],s=sign)
            soln3 = """a_n = a_(n-1) {s:s}{b:g}""".format(s=sign,b=coefficients[0])

        if form == 2:  # c - n^2 progression 
            func1 = constants[0] - Pow(x,2) #explicit formula
            for i in range(1,5):
                first_4_terms.append(round(float(func1.subs(x,i))),2)
            for i in range (5,8):
                next_3_terms.append(round(float(func1.subs(x,i))),2)
                
            soln2 = """a_n = {a:g} - n^2""".format(a=constants[0])
            soln3 = """a_n = a_(n-1)- (2n - 1)"""     
            
        
        self.question = problem
        self.soln = soln
        self.soln2 = soln2


print('GEOMETRIC PROGRESSION')
print()


 
for i in range (1,10):
    A = generalProgressionClass()
    print("P: " + str(stringHandling.cleanAst(A.question))) 
    print("""S1 {a:s}""".format(a=stringHandling.cleanAst(stringHandling.removeBrackets(str(A.soln)))))
    print("""S2 {a:s}""".format(a=stringHandling.cleanAst(stringHandling.removeBrackets(str(A.soln2)))))
    print()




stay = True
while stay:
    command = input()
    if command == 'exit':
        stay = False
