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


class absoluteValueInequalitiesClass:

    def __init__(self):
        #try:
        
        constants = []
        coefficients = []
        coeSmall = []
        oddNumbers = []
        evenNumbers = []
        relations = [' < ',' > ',' <= ',' >= ']
        setOperations = [' or ', ' and ']

        form = random.randint(1,3)
        
        for i in range(0,20):
            constants.append(round(random.randint(-40,40),2))
            if constants[i] == 0:
                constants.append(round(random.randint(1,200),2))
        
        for i in range(0,20):
            coefficients.append(round(random.randint(-9,9),2)) 
            if coefficients[i] == 0:
                constants.append(round(random.randint(1,9),2))
        if coefficients[1] == 0:
            coefficients[1] = random.randint(1,9)
        if coefficients[3] == 0:
            coefficients[3] = random.randint(1,9)
                
        if form == 1:
            exp1 = Abs(coefficients[0]*x + coefficients[1])
            exp2 = constants[0]
        
        if form == 2:   
            exp1 = Abs(coefficients[0]*x)
            exp2 = constants[0]
            
        if form == 3:
            exp1 = Abs(x/coefficients[0])
            exp2 = constants[0]
            
        temp = random.choice([0,1,2,3])
        
        if temp == 0:
            soln = solveset(exp1 - exp2 < 0 ,x ,S.Reals)
        if temp == 1:
            soln = solveset(exp1 - exp2 > 0, x, S.Reals)
        if temp == 2:
            soln = solveset(exp1 - exp2 <= 0, x, S.Reals)
        if temp == 3:
            soln = solveset(exp1 - exp2 >= 0, x, S.Reals)
        
        problem = str(exp1) + relations[temp] + str(temp)
        
        
        
        self.question = problem
        self.soln = soln
  
print('ABSOLUTE VALUE INEQUALITIES')
print()

for i in range (1,10):
    A = absoluteValueInequalitiesClass()
    print("P: " + str(stringHandling.cleanAst(A.question))) 
    print("""S1 {a:s}""".format(a=stringHandling.cleanAst(stringHandling.removeBrackets(str(A.soln)))))
    print()





stay = True
while stay:
    command = input()
    if command == 'exit':
        stay = False
