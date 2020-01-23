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


class compoundInequalitiesClass:

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
                
        if form == 1: #compound inequality with words 1
            exp1 = Add(coefficients[0]*x, coefficients[1]*x,evaluate = False)
            exp2 = constants[0]
            exp3 = Add(coefficients[2]*x, coefficients[3]*x,evaluate = False)
            exp4 = constants[1]    
            
        if form == 2: #compound inequality with words 2
            exp1 = coefficients[0]*x/coefficients[1]
            exp2 = constants[0]
            exp3 = coefficients[2]*x/coefficients[3]
            exp4 = constants[1]
        if form == 3: #compound inequality connected
            exp1 = constants[0]
            exp2 = coefficients[0]*x/coefficients[1]
            exp3 = constants[1]    
        
        if form == 1 or form == 2:
            temp2 = random.choice([0,1,2,3])
            if temp2 == 0:
                set1 = solveset(exp1 - exp2<0,x,S.Reals) 
            if temp2 == 1:
                set1 = solveset(exp1 - exp2>0,x,S.Reals) 
            if temp2 == 2:
                set1 = solveset(exp1 - exp2<=0,x,S.Reals) 
            if temp2 == 3:
                set1 = solveset(exp1 - exp2>=0,x,S.Reals) 
            
            temp3 = random.choice([0,1,2,3])
            if temp3 == 0:
                set2 = solveset(exp3 - exp4<0,x,S.Reals) 
            if temp3 == 1:
                set2 = solveset(exp3 - exp4>0,x,S.Reals) 
            if temp3 == 2:
                set2 = solveset(exp3 - exp4<=0,x,S.Reals) 
            if temp3 == 3:
                set2 = solveset(exp3 - exp4>=0,x,S.Reals)                     
        
            temp_and_or = random.choice([0,1])
            if temp_and_or == 0:
                soln = set1.union(set2)
            if temp_and_or == 1:
                soln = set1.intersect(set2)
            
            problem = str(exp1) + relations[temp2] + str(exp2) + setOperations[temp_and_or] + str(exp3) + relations[temp3] + str(exp4) 
        
        if form == 3:
            #select the relational operation
            temp2 = random.choice([0,1,2,3])
            if temp2 == 0:
                set1 = solveset(exp1 - exp2<0,x,S.Reals)
                set2 = solveset(exp3 - exp2<0,x,S.Reals) 
            if temp2 == 1:
                set1 = solveset(exp1 - exp2>0,x,S.Reals)
                set2 = solveset(exp3 - exp2>0,x,S.Reals)                
            if temp2 == 2:
                set1 = solveset(exp1 - exp2<=0,x,S.Reals) 
                set2 = solveset(exp3 - exp2<=0,x,S.Reals) 
            if temp2 == 3:
                set1 = solveset(exp1 - exp2>=0,x,S.Reals) 
                set2 = solveset(exp3 - exp2>=0,x,S.Reals) 
            
            soln = set1.union(set2)
            
            problem = str(exp1) + relations[temp2] + str(exp2) + relations[temp2] + str(exp3)

        self.question = problem
        self.soln = soln
  
print('COMPOUND INEQUALITIES')
print()

for i in range (1,10):
    A = compoundInequalitiesClass()
    print("P: " + str(stringHandling.cleanAst(A.question))) 
    print("""S1 {a:s}""".format(a=stringHandling.cleanAst(stringHandling.removeBrackets(str(A.soln)))))
    print()





stay = True
while stay:
    command = input()
    if command == 'exit':
        stay = False
