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
# import integral_calculus
# import analytic_geometry
# import differential_equations
# import algebra
# import physics
# import strength_of_materials as strength
import engineering_economy as econ

x, y = sym.symbols('x y', real = True)

import constants_conversions as c
from constants_conversions import *
from common_names import *




#test code
#from IPython.display import display
init_printing(use_unicode = False)
#display(yourobject) --- > to display new objects

solutions_flag = False

title_string = """Strength of Materials - Singer and PYtel
Coded by Leslie Caminade June 2019
www.lesliecaminadecom.wordpress.com
note: 
 - log(x) refers to the natural logarithm
 - constant of integration is not added by itself"""
 
questionList = (
econ.hipolito_2_1(),
econ.hipolito_2_2(),
econ.hipolito_2_3(),
#econ.hipolito_2_4(),
econ.hipolito_2_5(),
econ.hipolito_2_6(),
econ.hipolito_2_7(),
econ.hipolito_2_8(),
econ.hipolito_2_9(),
econ.hipolito_2_10(),
econ.hipolito_2_11(),
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
