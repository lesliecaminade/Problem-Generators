import randomizer
import random_handler as ran
import sympy_handler as symh
import numpy_handler as num
import sympy as sym
from sympy import init_printing
from sympy import oo
import math
import math_common
import random
import stringHandling
import integral_calculus
import analytic_geometry
import differential_equations
import algebra


x, y = sym.symbols('x y', real = True)
#n = s.symbols('n', real = True)

import constants_conversions as cc
from constants_conversions import *
from common_names import *




#test code
#from IPython.display import display
init_printing(use_unicode = False)
#display(yourobject) --- > to display new objects

solutions_flag = False

title_string = """Differential Equations 2 - Standard
Coded by Leslie Caminade 2019
www.lesliecaminadecom.wordpress.com
note: 
 - log(x) refers to the natural logarithm
 - constant of integration is not added by itself"""



class genericClass:

    def __init__(self):
        question = ""
        answer = ""
        
        solution = ""
       
        form = random.randint(1,8) #check
        #form = 8
        
        if form == 1: 
            deObject = differential_equations.solde_homo()
            question = deObject.question
            answer = deObject.answer
        if form == 2:
            deObject = differential_equations.solde_nonhomo_exp()
            question = deObject.question
            answer = deObject.answer
        if form == 3:
            deObject = differential_equations.solde_nonhomo_trig_solo()
            question = deObject.question
            answer = deObject.answer    
        if form == 4:
            deObject = differential_equations.solde_nonhomo_trig_duo()
            question = deObject.question
            answer = deObject.answer 
        if form == 5:
            deObject = differential_equations.solde_nonhomo_polynomial()
            question = deObject.question
            answer = deObject.answer     
        
        #if form == 6:
            #deObject = differential_equations.solde_nonhomo_vop1()
            #question = deObject.question
            #answer = deObject.answer          
        
        if form == 7:
            deObject = differential_equations.sonlde_homo_euler_cauchy()
            question = deObject.question
            answer = deObject.answer 
            
        if form == 8:
            deObject = differential_equations.RLC_circuits()
            question = deObject.question
            answer = deObject.answer 
            
        
            

        self.question = question
        self.answer = answer
        self.solution = solution

print(title_string)
print()

 
for i in range (1,30):
    A = genericClass()
    #display(A.question)
    #display(A.answer)
    print('--------------------------------------------')
    print(A.question)
    print(' ')
    print(A.answer)
    print(' ')
    print(' ')
    if solutions_flag == True:
        print("""solution: {a:s}""".format(a=str(A.solution)))
    print()
    



stay = True
while stay:
    command = input()
    if command == 'exit':
        stay = False
