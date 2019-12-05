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
#import energy_conversion as e
#import diodes as d
#import field_effect_transistors as fet
import operational_amplifiers as opamp
import power_amplifiers as poweramp

x, y = sym.symbols('x y', real = True)

import constants_conversions as c
from constants_conversions import *
from common_names import *




#test code
#from IPython.display import display
init_printing(use_unicode = False)
#display(yourobject) --- > to display new objects

solutions_flag = False

title_string = """Operational and Power Amplifiers
Coded by Leslie Caminade June 2019
www.lesliecaminadecom.wordpress.com"""

questionList = (
opamp.boylestad_10_1(),
opamp.boylestad_10_2(),
opamp.boylestad_10_3(),
opamp.boylestad_10_4(),
opamp.boylestad_10_5(),
opamp.boylestad_10_6(),
opamp.boylestad_10_7(),
opamp.boylestad_10_8(),
opamp.boylestad_10_9(),
opamp.boylestad_10_10(),
opamp.boylestad_10_11(),
opamp.boylestad_10_12(),
opamp.boylestad_10_13(),
opamp.boylestad_10_14(),
opamp.boylestad_10_15(),
#opamp.boylestad_10_16(),
opamp.boylestad_10_17(),
opamp.boylestad_10_22(),
opamp.boylestad_11_1(),
opamp.boylestad_11_2(),
opamp.boylestad_11_3(),
opamp.boylestad_11_6(),
opamp.boylestad_11_7(),
opamp.boylestad_11_8(),
opamp.boylestad_11_10(),
opamp.boylestad_11_11(),
opamp.boylestad_11_12(),
opamp.boylestad_11_13(),
opamp.boylestad_11_14(),
poweramp.boylestad_12_1(),
poweramp.boylestad_12_2(),
poweramp.boylestad_12_3(),
poweramp.boylestad_12_6(),
poweramp.boylestad_12_7(),
poweramp.boylestad_12_8(),
poweramp.boylestad_12_9(),
poweramp.boylestad_12_10(),
poweramp.boylestad_12_11(),
poweramp.boylestad_12_12(),
poweramp.boylestad_12_13(),
poweramp.boylestad_12_15(),
poweramp.boylestad_12_16(),
poweramp.boylestad_12_17(),
poweramp.boylestad_12_18()
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
