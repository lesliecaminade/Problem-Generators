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

title_string = """Newton's Law - Chapter 3 - Schaum's Outline
Coded by Leslie Caminade 2019
Last Updated June 26 2019
www.lesliecaminadecom.wordpress.com
note: 
 - log(x) refers to the natural logarithm
 - constant of integration is not added by itself"""
questionList = (
physics.example_3_1(),
physics.example_3_2(),
physics.example_3_3(),
physics.example_3_4(),
physics.example_3_5(),
physics.example_3_6(),
physics.example_3_7(),
physics.example_3_8(),
physics.example_3_9(),
physics.example_3_10(),
physics.example_3_11(),
physics.example_3_13(),
physics.example_3_14(),
physics.example_3_15(),
physics.example_3_16(),
physics.example_3_17(),
physics.example_3_18(),
physics.example_3_19(),
physics.example_3_20(),
physics.example_3_21(),
physics.example_3_22(),
physics.example_3_23(),
physics.example_3_24()
)

#populate a set of all the items
total_items_list = []
for i in range(len(questionList)):
    total_items_list.append(i)
    
    
#choose a smaller subset from these questions
items_list = random.sample(total_items_list, round(0.9 * len(questionList)))


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
