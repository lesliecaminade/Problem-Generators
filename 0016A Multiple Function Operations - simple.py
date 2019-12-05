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



class multipleFunctionsClass:

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
            coefficients.append(round(random.randint(-9,9),2)) 
            if coefficients[i] == 0:
                constants.append(round(random.randint(1,9),2))
        
        for i in range(0,20):
            powers.append(round(random.randint(1,3),2)) 
            if coefficients[i] == 0:
                constants.append(round(random.randint(1,3),2))
        
        #expression_to_substitute = coefficients[11]*x + coefficients[12]
        number_to_substitute = random.randint(-9,9)
        
        if form == 1:
            func1 = Pow(x,2) + coefficients[0]*x + coefficients[1]
            func2 = coefficients[2]*x + coefficients[3]
            
        if form == 2:
            func1 = Pow(x,3) + coefficients[0]*x
            func2 = Pow(x,2) + coefficients[0]*x + coefficients[1]
            
        if form == 3:
            func1 = coefficients[0]*Pow(x,2) + coefficients[1]
            func2 = func2 = Pow(x,2) + coefficients[0]*x + coefficients[1]
            
        if form == 4:
            func1 = coefficients[0]*x + coefficients[1]
            func2 = coefficients[2]*x + coefficients[3]
            
        if form == 5:
            func1 = coefficients[0]*x + coefficients[1]
            func2 = Pow(x,3) + coefficients[2]*x
            
        operations = random.choice([0,1,2,3])
        #operations = 0 #temp
        if operations == 0:#simple addition
            soln = func1.subs(x,number_to_substitute) + func2.subs(x,number_to_substitute)
            
            temp = random.randint(0,1)
            if temp == 0:
                problem = """f(x) = {a:s}
g(x) = {b:s}
Find f({c:s}) + g({c:s})
                """.format(a = str(func1),b = str(func2), c = str(number_to_substitute))
            if temp == 1:
                problem = """f(x) = {a:s}
g(x) = {b:s}
Find (f+g)({c:s})
                """.format(a = str(func1),b = str(func2), c = str(number_to_substitute))

        if operations == 1:#simple multiplication
            soln = func1.subs(x,number_to_substitute) * func2.subs(x,number_to_substitute)
            
            problem = """f(x) = {a:s}
g(x) = {b:s}
Find (f•g)({c:s})
            """.format(a = str(func1),b = str(func2), c = str(number_to_substitute))  

        if operations == 2:#simple division
            soln = func1.subs(x,number_to_substitute) / func2.subs(x,number_to_substitute)
            
            problem = """f(x) = {a:s}
g(x) = {b:s}
Find (f/g)({c:s})
            """.format(a = str(func1),b = str(func2), c = str(number_to_substitute))              

        if operations == 3:#composition
            partial_solution = func2.subs(x,number_to_substitute)
            soln = func1.subs(x,partial_solution)
            
            temp = random.randint(0,1)
            if temp == 0:
                problem = """f(x) = {a:s}
g(x) = {b:s}
Find (f°g)({c:s})
                """.format(a = str(func1),b = str(func2), c = str(number_to_substitute))
            if temp == 1:
                problem = """f(x) = {a:s}
g(x) = {b:s}
Find (f(g({c:s})))
                """.format(a = str(func1),b = str(func2), c = str(number_to_substitute))
                
            if operations == 4:#subtraction
                soln = func1.subs(x,number_to_substitute) + func2.subs(x,number_to_substitute)
                
                temp = random.randint(0,1)
                if temp == 0:
                    problem = """f(x) = {a:s}
    g(x) = {b:s}
    Find f({c:s}) - g({c:s})
                    """.format(a = str(func1),b = str(func2), c = str(number_to_substitute))
                if temp == 1:
                    problem = """f(x) = {a:s}
    g(x) = {b:s}
    Find (f-g)({c:s})
                    """.format(a = str(func1),b = str(func2), c = str(number_to_substitute))
                
        self.question = problem
        self.soln = expand(soln)
  
print('MULTIPLE FUNCTION OPERATIONS')
print()

for i in range (1,10):
    A = multipleFunctionsClass()
    print("P: " + str(stringHandling.cleanAst(A.question))) 
    print("""S1 {a:s}""".format(a=stringHandling.cleanAst(stringHandling.removeBrackets(str(A.soln)))))
    print()





stay = True
while stay:
    command = input()
    if command == 'exit':
        stay = False
