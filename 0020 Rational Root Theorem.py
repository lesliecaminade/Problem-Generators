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



class rationalRootTheoremClass:

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
        
        form = random.randint(2,6)

        for i in range(0,20):
            constants.append(round(random.randint(-40,40),2))
            if constants[i] == 0:
                constants.append(round(random.randint(1,200),2))
        
        for i in range(0,20):
            coefficients.append(round(random.randint(-19,19),2)) 
            if coefficients[i] == 0:
                constants.append(round(random.randint(1,9),2))
        
        for i in range(0,20):
            powers.append(round(random.randint(1,3),2)) 
            if coefficients[i] == 0:
                constants.append(round(random.randint(1,4),2))
        
        
        if form == 2:
            func1 = coefficients[2]*Pow(x,2) + coefficients[1]*Pow(x,1) + coefficients[0]
            
        if form == 3:
            func1 = coefficients[3]*Pow(x,3) + coefficients[2]*Pow(x,2) + coefficients[1]*Pow(x,1) + coefficients[0]

        if form == 4:
            func1 = coefficients[4]*Pow(x,4) + coefficients[3]*Pow(x,3) + coefficients[2]*Pow(x,2) + coefficients[1]*Pow(x,1) + coefficients[0]

        if form == 5:
            func1 = coefficients[5]*Pow(x,5) + coefficients[4]*Pow(x,4) + coefficients[3]*Pow(x,3) + coefficients[2]*Pow(x,2) + coefficients[1]*Pow(x,1) + coefficients[0]                

        if form == 6:
            func1 = coefficients[6]*Pow(x,6) +coefficients[5]*Pow(x,5) + coefficients[4]*Pow(x,4) + coefficients[3]*Pow(x,3) + coefficients[2]*Pow(x,2) + coefficients[1]*Pow(x,1) + coefficients[0]   
            
        factors_of_leading_coefficient = []
        factors_of_constant_term = []
        
        coefficient_leading = coefficients[form]
        for i in range(1,100):
            modulo = coefficient_leading%i
            if modulo == 0:
                factors_of_leading_coefficient.append(i)
        
        constant_term = coefficients[0]
        for i in range(1,100):
            modulo = constant_term%i
            if modulo == 0:
                factors_of_constant_term.append(i)  
        
        rational_roots = []
        problem = str(func1)
        for i in range(0,len(factors_of_leading_coefficient)):
            for j in range(0,len(factors_of_constant_term)):
                rational_roots.append(Rational(factors_of_leading_coefficient[i],factors_of_constant_term[j]))
            
        self.question = problem + ' = 0'
        self.soln = 'Rational Numerator(s): ' + str(factors_of_leading_coefficient)
        self.soln2 = 'Rational Denominator(s): ' + str(factors_of_constant_term)
        self.soln3 = 'Possible Rational Root(s) ±: ' + str(rational_roots)

print('RATIONAL ROOT THEOREM')
print()



for i in range (1,10):
    A = rationalRootTheoremClass()
    print("P: " + str(stringHandling.cleanAst(A.question))) 
    print("""S1 {a:s}""".format(a=stringHandling.cleanAst(stringHandling.removeBrackets(str(A.soln)))))
    print("""S2 {a:s}""".format(a=stringHandling.cleanAst(stringHandling.removeBrackets(str(A.soln2)))))
    print("""S3 {a:s}""".format(a=stringHandling.cleanAst(stringHandling.removeBrackets(str(A.soln3)))))
    print()




stay = True
while stay:
    command = input()
    if command == 'exit':
        stay = False
