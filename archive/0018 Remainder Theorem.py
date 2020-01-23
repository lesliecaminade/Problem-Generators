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



class remainderTheoremClass:

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
        
        form = random.randint(1,4)

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
        
        func2 = x - coefficients[11]
        
        if form == 1:
            func1 = coefficients[0]*Pow(x,3) + coefficients[1]*Pow(x,2) + coefficients[2]*Pow(x,1) + coefficients[3]
            
        if form == 2:
            func1 = coefficients[0]*Pow(x,2) + coefficients[1]*Pow(x,1) + coefficients[2]  
            
        if form == 3:
            func1 = coefficients[0]*Pow(x,4) + coefficients[1]*Pow(x,3) + coefficients[2]*Pow(x,2) + coefficients[3]*x + coefficients[4]
            
        if form == 4:
            func1 = coefficients[0]*Pow(x,5) + coefficients[1]*Pow(x,4) + coefficients[2]*Pow(x,3) + coefficients[3]*Pow(x,2) + coefficients[4]*x + coefficients[5]  
            
        problem = '('+str(func1) + ') ÷ (' + str(func2) + ')'
        quotient = div(func1,func2)[0]
        remainder = div(func1,func2)[1]
        #remainder = func1.subs(x, coefficients[11])
        self.question = problem
        self.soln = quotient
        self.soln2 = remainder
  
print('REMAINDER THEOREM')
print()
  
  
for i in range (1,10):
    A = remainderTheoremClass()
    print("P: " + str(stringHandling.cleanAst(A.question))) 
    print("""Q: {a:s}""".format(a=stringHandling.cleanAst(stringHandling.removeBrackets(str(A.soln)))))
    print("""R: {a:s}""".format(a=stringHandling.cleanAst(stringHandling.removeBrackets(str(A.soln2)))))
    #print("""trap: {a:s}""".format(a=str(A.trap))) 
    print()




stay = True
while stay:
    command = input()
    if command == 'exit':
        stay = False
