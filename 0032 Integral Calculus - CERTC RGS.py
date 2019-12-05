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

title_string = """Integral Calculus - RGS CERTC
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
       
        form = random.randint(1,12) #check
        #form = 12
        
        if form == 1: 
            fobject = integral_calculus.basic_1()
            f = fobject.expression
            fp = sym.pretty(f)
            fa = fobject.answer
            question = f"""Evaluate
{fp}"""
            answer = f"""{fa} + C"""    
            
        if form == 2: 
            fobject = integral_calculus.basic_2()
            f = fobject.expression
            fp = sym.pretty(f)
            fa = fobject.answer
            question = f"""Evaluate
{fp}"""            
            answer = f"""{fa} + C"""   
        
        if form == 3:
            fobject = integral_calculus.basic_3()
            f = fobject.expression
            fp = sym.pretty(f)
            fa = fobject.answer
            question = f"""Evaluate
{fp}"""            
            answer = f"""{fa} + C""" 
        
        if form == 4:
            fobject = integral_calculus.multiple_1()
            f = fobject.expression
            fp = sym.pretty(f)
            fa = fobject.answer
            question = f"""Evaluate
{fp}"""   
            answer = f"""{fa}""" 
            
        if form == 5:
            fobject = integral_calculus.multiple_2()
            f = fobject.expression
            fp = sym.pretty(f)
            fa = fobject.answer
            question = f"""Evaluate
{fp}"""   
            answer = f"""{fa}""" 
            
        
        if form == 6:
            pobject = integral_calculus.area_1()
            question = pobject.problem
            answer = pobject.answer

            
        if form == 7:
            pobject = integral_calculus.area_2()
            question = pobject.problem
            answer = pobject.answer
#--------------------------stopped here-----------------------------------#
        if form == 8:
            problemObject = integral_calculus.area_3()
            question = problemObject.problem_area
            answer = problemObject.answer_area
            
        if form == 9:
            problemObject = integral_calculus.area_4()
            question = problemObject.problem
            answer = problemObject.answer
            
        if form == 10:
            problemObject = integral_calculus.area_5()
            question = problemObject.problem_area
            answer = problemObject.answer_area
        
        if form == 11:
            problemObject = integral_calculus.area_3()
            question = problemObject.problem_centroid
            answer = problemObject.answer_centroid
            
        if form == 12:
            problemObject = integral_calculus.area_5()
            question = problemObject.problem_centroid
            answer = problemObject.answer_centroid
            
        if form == 13:
            problemObject = integral_calculus.length_of_arc_1()
            question = problemObject.problem
            answer = problemObject.answer
            
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
