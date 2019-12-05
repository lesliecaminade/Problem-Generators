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



class arithmeticProgressionClass:

    def __init__(self):
        #try:
        
        constants = []
        coefficients = []
        powers= []
        coeSmall = []
        oddNumbers = []
        evenNumbers = []
        relations = [' < ',' > ',' <= ',' >= ']
        functionOperations = [' + ',' - ',' • ', ' / ' ,' ° ']
        
        form = random.randint(1,2)
        
        integers_or_decimals = random.randint(0,1)
        
        if integers_or_decimals == 0:
            for i in range(0,20):
                coefficients.append(round(random.randint(-19,19),2)) 
 
        elif integers_or_decimals == 1:
            for i in range(0,20):
                coefficients.append(round(random.uniform(-19,19),2)) 
 
        
        
        random_n = random.randint(1,50)
        func1 = coefficients[0] + coefficients[1]*x
        first_4_terms = []
        for i in range(1,5):
            first_4_terms.append(round(func1.subs(x,i),2))
            
        random_term = round(float(func1.subs(x,random_n)),2)
        soln = str(first_4_terms)
        
        
        if form == 1: 
            soln2 = str(random_term)
            problem = """Find the first 4 terms and the stated term given the arithmetic sequence, with a_1 as the first term:
            a_n = {a:g} + {b:g}n, a_{c:g}""".format(a=coefficients[0],b=coefficients[1],c=random_n)

        if form == 2:
            soln2 = """a_n = {a:g} + {b:g}n""".format(a=coefficients[0],b=coefficients[1])
            
            problem = """Given the first term and common difference, find the first four terms and the formula:
            a_1 = {a:g}, d = {b:g}""".format(a=coefficients[0],b=coefficients[1])
            
            
        self.question = problem
        self.soln = soln
        self.soln2 = soln2


print('ARITHMETIC PROGRESSION')
print()


 
for i in range (1,10):
    A = arithmeticProgressionClass()
    print("P: " + str(stringHandling.cleanAst(A.question))) 
    print("""S1 {a:s}""".format(a=stringHandling.cleanAst(stringHandling.removeBrackets(str(A.soln)))))
    print("""S2 {a:s}""".format(a=stringHandling.cleanAst(stringHandling.removeBrackets(str(A.soln2)))))
    print()




stay = True
while stay:
    command = input()
    if command == 'exit':
        stay = False
