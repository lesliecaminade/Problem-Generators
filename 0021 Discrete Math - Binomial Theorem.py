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



class binomialTheoremClass:

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
        
        form = random.randint(1,5)
        
            
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
                constants.append(round(random.randint(1,9),2))
        
        if form == 1: 
            func1 = coefficients[0]*x + coefficients[1]
            power = random.randint(1,9)
            func2 = Pow(func1,power)
        if form == 2: 
            func1 = coefficients[0]*x + coefficients[1]*y
            power = random.randint(1,9)
            func2 = Pow(func1,power)                
        if form == 3: 
            func1 = coefficients[0]*Pow(x,random.randint(1,9)) + coefficients[1]
            power = random.randint(1,9)
            func2 = Pow(func1,power)
        if form == 4: 
            func1 = coefficients[0]*Pow(x,random.randint(1,9)) + coefficients[1]*Pow(y,random.randint(1,9))
            power = random.randint(1,9)
            func2 = Pow(func1,power)
        if form == 5: 
            func1 = coefficients[0]*Pow(x,random.randint(1,9)) + coefficients[1]*(1/Pow(x,random.randint(1,9)))
            power = random.randint(1,9)
            func2 = Pow(func1,power)
        
        problem = str(func2)
        soln = expand(func2)
            
        self.question = problem
        self.soln = 'Full Binomial Expansion: ' + str(soln)
        self.soln2 = 'The coefficient of x^n in the expansion...'
        self.soln3 = 'The nth term of the expansion...'

print('BINOMIAL THEOREM')
print()


 
for i in range (1,10):
    A = binomialTheoremClass()
    print("P: " + str(stringHandling.cleanAst(A.question))) 
    print("""S1 {a:s}""".format(a=stringHandling.cleanAst(stringHandling.removeBrackets(str(A.soln)))))

    print()




stay = True
while stay:
    command = input()
    if command == 'exit':
        stay = False
