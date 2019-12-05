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
# import engineering_economy as econ
import energy_conversion as e

x, y = sym.symbols('x y', real = True)

import constants_conversions as c
from constants_conversions import *
from common_names import *




#test code
#from IPython.display import display
init_printing(use_unicode = False)
#display(yourobject) --- > to display new objects

solutions_flag = False

title_string = """Energy Conversion
Coded by Leslie Caminade June 2019
www.lesliecaminadecom.wordpress.com
note: 
 - log(x) refers to the natural logarithm
 - constant of integration is not added by itself"""

questionList = (
e.johnbird_4_1(),
e.johnbird_4_2(),
e.johnbird_4_3(),
e.johnbird_4_4(),
e.johnbird_21_1(),
e.johnbird_21_2(),
e.johnbird_21_3(),
e.johnbird_21_4(),
e.johnbird_21_5(),
e.johnbird_21_6(),
e.johnbird_21_7(),
e.johnbird_21_8(),
e.johnbird_21_9(),
e.johnbird_21_10(),
e.johnbird_21_11(),
e.johnbird_21_12(),
e.johnbird_21_13(),
e.johnbird_22_1(),
e.johnbird_22_2(),
e.johnbird_22_3(),
e.johnbird_22_4(),
e.johnbird_22_5(),
e.johnbird_22_6(),
e.johnbird_22_7(),
e.johnbird_22_8(),
e.johnbird_22_9(),
e.johnbird_22_10(),
e.johnbird_22_11(),
e.johnbird_22_12(),
e.johnbird_22_13(),
e.johnbird_22_14(),
e.johnbird_22_15(),
e.johnbird_22_16(),
e.johnbird_22_17(),
e.johnbird_22_18(),
e.johnbird_22_19(),
e.johnbird_22_20(),
e.johnbird_22_21(),
e.johnbird_22_22(),
e.johnbird_22_23(),
e.johnbird_22_24(),
e.johnbird_22_25(),
e.johnbird_22_26(),
e.johnbird_22_27(),
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
