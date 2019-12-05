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



class descartesRuleOfSignsClass:

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
        
        form =random.randint(2,6)

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
        
        substituted_by_negative_x_coefficients = [None]*20
        
        for i in range(1,20,2):
            substituted_by_negative_x_coefficients[i] = -coefficients[i]
        for i in range(0,20,2):
            substituted_by_negative_x_coefficients[i] = coefficients[i]
        
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
            
        previous_sign = 0 #saves the sign of the prev coefficient
        positive_alternations = 0
        coefficient_index = form
        negative_alternations = 0
        
        if coefficients[coefficient_index]>0:
            previous_sign = 1
        else:
            previous_sign = 0
        
        coefficient_index = coefficient_index - 1
        while coefficient_index >= 0:
            if previous_sign == 1 and coefficients[coefficient_index] < 0:
                positive_alternations = positive_alternations + 1
                previous_sign = 0
            if previous_sign == 0 and coefficients[coefficient_index] >= 0:
                positive_alternations = positive_alternations + 1
                previous_sign = 1
            coefficient_index = coefficient_index - 1
        
        coefficient_index = form
        if substituted_by_negative_x_coefficients[coefficient_index]>0:
            previous_sign = 1
        else:
            previous_sign = 0
        
        coefficient_index = coefficient_index - 1
        while coefficient_index >= 0:
            if previous_sign == 1 and substituted_by_negative_x_coefficients[coefficient_index] < 0:
                negative_alternations = negative_alternations + 1
                previous_sign = 0
            if previous_sign == 0 and substituted_by_negative_x_coefficients[coefficient_index] >= 0:
                negative_alternations = negative_alternations + 1
                previous_sign = 1
            coefficient_index = coefficient_index - 1

            
        problem = str(func1)
        positive_alternations_list = []
        negative_alternations_list = []
        i = positive_alternations
        j = negative_alternations
        
        while i >= 0:
            positive_alternations_list.append(i)
            i = i - 2
        while j >= 0:
            negative_alternations_list.append(j)
            j = j - 2
        soln = positive_alternations_list
        soln2 = negative_alternations_list


        self.question = problem + ' = 0'
        self.soln = 'Positive roots: ' + str(soln)
        self.soln2 = 'Negative roots: ' + str(soln2)

print('DESCARTES RULE OF SIGNS')
print()

for i in range (1,10):
    A = descartesRuleOfSignsClass()
    print("P: " + str(stringHandling.cleanAst(A.question))) 
    print("""S1 {a:s}""".format(a=stringHandling.cleanAst(stringHandling.removeBrackets(str(A.soln)))))
    print("""S2 {a:s}""".format(a=stringHandling.cleanAst(stringHandling.removeBrackets(str(A.soln2)))))
    print()




stay = True
while stay:
    command = input()
    if command == 'exit':
        stay = False
