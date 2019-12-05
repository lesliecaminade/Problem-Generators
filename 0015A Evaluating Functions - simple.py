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



class simpleFunctionsClass:

    def __init__(self):
        #try:
        
        constants = []
        coefficients = []
        powers= []
        coeSmall = []
        oddNumbers = []
        evenNumbers = []
        relations = [' < ',' > ',' <= ',' >= ']
        setOperations = [' or ', ' and ']
        
        form = random.randint(1, 7)
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
                constants.append(round(random.randint(1,3),2))
        
        if coefficients[1] == 0:
            coefficients[1] = random.randint(1,9)
        if coefficients[3] == 0:
            coefficients[3] = random.randint(1,9)
        
        number_to_substitute = random.randint(-9,9)
        
        if form == 1:
            func1 = coefficients[0]*Pow(x,2) + coefficients[1]
            
        if form == 2:   
            func1 = coefficients[0]*Pow(x,2) + coefficients[1]*x
        
        if form == 3:
            func1 = Pow(coefficients[0], x + powers[0])
        
        if form == 4:
            func1 = coefficients[0]*x
        
        if form == 5:
            func1 = coefficients[0]*Pow(x,3) + coefficients[1]*Pow(x,2)
            
        if form == 6:
            func1 = Pow(coefficients[0], powers[1]*x)
            
        if form == 7:
            func1 = coefficients[0]*Pow(x,2) + coefficients[1]
        
        problem = 'f(x) = ' + str(func1) + ', Find f(' + str(number_to_substitute) + ')'
        soln = func1.subs(x,number_to_substitute)
        self.question = problem
        self.soln = soln
  
print('SIMPLE FUNCTIONS')
print()

for i in range (1,10):
    A = simpleFunctionsClass()
    print("P: " + str(stringHandling.cleanAst(A.question))) 
    print("""S1 {a:s}""".format(a=stringHandling.cleanAst(stringHandling.removeBrackets(str(A.soln)))))
    print()





stay = True
while stay:
    command = input()
    if command == 'exit':
        stay = False
