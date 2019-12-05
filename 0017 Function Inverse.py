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



class inverseFunctionClass:

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
        
        form = random.randint(1,6)

        for i in range(0,20):
            constants.append(round(random.randint(-40,40),2))
            if constants[i] == 0:
                constants.append(round(random.randint(1,200),2))
        
        for i in range(0,20):
            coefficients.append(round(random.randint(-9,9),2)) 
            if coefficients[i] == 0:
                constants.append(round(random.randint(1,9),2))
        
        for i in range(0,20):
            powers.append(round(random.randint(1,3),2)) 
            if coefficients[i] == 0:
                constants.append(round(random.randint(1,4),2))
        
        if form == 1:
            func1 = Rational(coefficients[0],coefficients[1])*x + coefficients[2]
        if form == 2: 
            func1 = coefficients[0]*x + coefficients[1]
        if form == 3: 
            func1 = coefficients[0]*Pow((x + coefficients[1]),powers[0])
        if form == 4:
            func1 = (coefficients[0] + coefficients[1]*x)/(coefficients[2])
        if form == 5:
            func1 = Pow(x + coefficients[0],powers[0])
        if form == 6:
            func1 = coefficients[0]*x
            
        problem = 'f(x) = '+ str(func1)
        soln = solveset( y - func1, x, S.Reals)
        soln = soln.subs(y,x)
        soln = 'f^-1(x) = ' + str(soln)
        #soln = soln.replace('y','x')
        self.question = problem
        self.soln = soln
  
print('INVERSE FUNCTIONS')
print()

for i in range (1,10):
    A = inverseFunctionClass()
    print("P: " + str(stringHandling.cleanAst(A.question))) 
    print("""S1 {a:s}""".format(a=stringHandling.cleanAst(stringHandling.removeBrackets(str(A.soln)))))
    print()





stay = True
while stay:
    command = input()
    if command == 'exit':
        stay = False
