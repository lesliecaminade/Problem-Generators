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


class multipleStepInequalitiesClass:

    def __init__(self, form):
        #try:
        
        constants = []
        coefficients = []
        coeSmall = []
        oddNumbers = []
        evenNumbers = []
        relations = ['<','>','>=','<=']

        for i in range(0,20):
            constants.append(round(random.randint(-200,200),2))
            if constants[i] == 0:
                constants.append(round(random.randint(1,200),2))
        
        for i in range(0,20):
            coefficients.append(round(random.randint(-9,9),2)) 
            if coefficients[i] == 0:
                constants.append(round(random.randint(1,9),2))
        
        relation = random.choice(relations)
        
        if form == 1:
            exp1 = Add(coefficients[0]*x, coefficients[1]*x,evaluate = False)
            exp2 = constants[0]
        
        if form == 2:
            exp1 = Add(coefficients[0]*x, constants[0],evaluate = False)
            exp2 = Mul(coefficients[1],(coefficients[2] + coefficients[3]*x),evaluate=False) + coefficients[4]*x
        
        if form == 3:
            exp1 = constants[0]
            exp2 = Add(coefficients[0]*x,constants[1],coefficients[1]*x,evaluate=False)

        if form == 4:
            exp1 = Mul(coefficients[0],coefficients[1] + coefficients[2]*x,evaluate=False)
            exp2 = coefficients[3]*x + constants[0]
  
        heads_or_tails = random.randint(0,1)
        if heads_or_tails == 1:
            temp = exp2
            exp2 = exp1
            exp1 = temp
        
        problem = str(exp1) +' '+ relation +' '+ str(exp2)
        soln = solve_poly_inequality(Poly(exp1 - exp2),relation)    
        
        self.question = problem
        self.soln = soln
  
for i in range (1,10):
    A = multipleStepInequalitiesClass(random.randint(1,4))
    print("problem: " + str(stringHandling.cleanAst(A.question))) 
    print("""answer: {a:s}""".format(a=str(A.soln)))
    #print("""trap: {a:s}""".format(a=str(A.trap))) 
    print()




stay = True
while stay:
    command = input()
    if command == 'exit':
        stay = False
