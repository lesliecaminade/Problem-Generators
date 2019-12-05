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
import physics
# import strength_of_materials as strength
#import engineering_economy as econ

x, y = sym.symbols('x y', real = True)

import constants_conversions as c
from constants_conversions import *
from common_names import *




#test code
#from IPython.display import display
init_printing(use_unicode = False)
#display(yourobject) --- > to display new objects

solutions_flag = False

title_string = """Thermodynamics
Schaums, ...
Coded by Leslie Caminade June 2019
June 26 2019 - Changed the way questions are selected.
www.lesliecaminadecom.wordpress.com
note: 
 - log(x) refers to the natural logarithm
 - constant of integration is not added by itself"""

questionList = (
physics.schaums_15_1(),
physics.schaums_15_2(),
physics.schaums_15_3(),
physics.schaums_15_4(),
physics.schaums_15_5(),
physics.schaums_15_6(),
physics.schaums_15_7(),
physics.schaums_15_8(),
physics.schaums_15_9(),
physics.schaums_15_10(),
physics.schaums_16_1(),
physics.schaums_16_2(),
physics.schaums_16_3(),
physics.schaums_16_4(),
physics.schaums_16_5(),
physics.schaums_16_6(),
physics.schaums_16_7(),
physics.schaums_16_8(),
physics.schaums_16_9(),
physics.schaums_16_10(),
physics.schaums_16_11(),
physics.schaums_16_12(),
physics.schaums_16_13(),
physics.schaums_16_14(),
physics.schaums_16_15(),
physics.schaums_16_16(),
physics.schaums_16_17(),
physics.schaums_16_18(),
physics.schaums_17_1(),
physics.schaums_17_2(),
physics.schaums_17_3(),
physics.schaums_17_4(),
physics.schaums_17_5(),
physics.schaums_17_6(),
physics.schaums_17_7(),
physics.schaums_17_8(),
physics.schaums_17_9(),
physics.schaums_17_10(),
physics.schaums_17_11(),
physics.schaums_17_12(),
physics.schaums_18_1(),
physics.schaums_18_2(),
physics.schaums_18_3(),
physics.schaums_18_4(),
physics.schaums_18_5(),
physics.schaums_18_6(),
physics.schaums_18_7(),
physics.schaums_18_8(),
physics.schaums_18_9(),
physics.schaums_18_10(),
physics.schaums_18_11(),
physics.schaums_18_12(),
physics.schaums_18_13(),
physics.schaums_18_14(),
physics.schaums_18_15(),
physics.schaums_18_16(),
physics.schaums_18_17(),
physics.schaums_18_18(),
physics.schaums_19_1(),
physics.schaums_19_2(),
physics.schaums_19_3(),
physics.schaums_19_4(),
physics.schaums_19_5(),
physics.schaums_19_6(),
physics.schaums_19_7(),
physics.schaums_19_8(),
physics.schaums_20_1(),
physics.schaums_20_1(),
physics.schaums_20_2(),
physics.schaums_20_3(),
physics.schaums_20_4(),
physics.schaums_20_5(),
physics.schaums_20_6(),
physics.schaums_20_7(),
physics.schaums_20_8(),
physics.schaums_20_9(),
physics.schaums_20_10(),
physics.schaums_20_11(),
physics.schaums_20_12(),
physics.schaums_20_13(),
physics.schaums_20_14(),
physics.schaums_20_15(),
physics.schaums_20_16()
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
