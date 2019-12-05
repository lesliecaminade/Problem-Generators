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
import physics

x, y = sym.symbols('x y', real = True)

import constants_conversions as c
from constants_conversions import *
from common_names import *




#test code
#from IPython.display import display
init_printing(use_unicode = False)
#display(yourobject) --- > to display new objects

solutions_flag = False

title_string = """Simple Harmonic Motion - Schaums Chapter 11
Coded by Leslie Caminade 2019
www.lesliecaminadecom.wordpress.com
note: 
 - log(x) refers to the natural logarithm
 - constant of integration is not added by itself"""
questionList = (
physics.schaums_11_2(),#0
physics.schaums_11_3(),#1
physics.schaums_11_4(),#2
physics.schaums_11_5(),#3
physics.schaums_11_6(),
physics.schaums_11_7(),
physics.schaums_11_8(),
physics.schaums_11_10(),
physics.schaums_11_11(),
physics.schaums_11_13(),
physics.schaums_11_14(),
physics.schaums_11_17()
)

#populate a set of all the items
total_items_list = []
for i in range(len(questionList)):
    total_items_list.append(i)
    
    
#choose a smaller subset from these questions
items_list = random.sample(total_items_list, round(0.25 * len(questionList)))


print(title_string)
print()
print(items_list)

for i in range (len(items_list)):
    print('-----------------------------------------------------------------------')
    item = questionList[items_list[i]]
    print(item.question)
    print()
    print(item.answer)
    



stay = True
while stay:
    command = input()
    if command == 'exit':
        stay = False
