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
import differential_equations as d
import algebra


x, y = sym.symbols('x y', real = True)
#n = s.symbols('n', real = True)

import constants_conversions as c
from constants_conversions import *
from common_names import *

init_printing(use_unicode = False)


solutions_flag = False

title_string = """Differential Equations 1  - First Order
Coded by Leslie Caminade June 2019
www.lesliecaminadecom.wordpress.com
note: 
 - log(x) refers to the natural logarithm
 - constant of integration is not added by itself"""


class genericClass:

    def __init__(self):
        question = ""
        answer = ""
        
        solution = ""
        
        questionList = (
        d.rainville_separable(),
        )
        
        temp = random.randint(0,len(questionList)-1)
        try:
            q = questionList[temp]
            self.question = q.question
            self.answer = q.answer
            try:
                self.choices = q.choices
            except:
                self.choices = ''
            
            try:
                self.solution = q.solution
                
            except:
                self.solution = 'no solution provided'
        except:
            pass

            



print(title_string)
print()

for i in range (1,200):
    A = genericClass()
    print('--------------------------------------------')
    print(A.question)
    print(' ')
    #print(A.choices)
    #print(' ')
    print(A.answer)
    print(' ')

    if solutions_flag == True:
        print("""solution: {a:s}""".format(a=str(A.solution)))
    print()

    



stay = True
while stay:
    command = input()
    if command == 'exit':
        stay = False
