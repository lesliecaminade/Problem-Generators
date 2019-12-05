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

title_string = """Work Energy and Power:
Schaums, Serway...
Coded by Leslie Caminade 2019
June 26 2019 - Added serway chapters 7 and 8
www.lesliecaminadecom.wordpress.com
note: 
 - log(x) refers to the natural logarithm
 - constant of integration is not added by itself"""

questionList = (
physics.schaums_6_1(),
physics.schaums_6_2(),
physics.schaums_6_3(),
physics.schaums_6_4(),
physics.schaums_6_6(),
physics.schaums_6_7(),
physics.schaums_6_8(),
physics.schaums_6_9(),
physics.schaums_6_10(),
physics.schaums_6_11(),
physics.schaums_6_13(),
physics.schaums_6_16(),
physics.schaums_6_17(),
physics.schaums_6_18(),
physics.schaums_6_19(),
physics.schaums_6_20(),
physics.schaums_6_21(),
physics.schaums_6_23(),
physics.serway_7_1(),
physics.serway_7_3(),
physics.serway_7_5(),
physics.serway_7_6(),
physics.serway_8_3(),
physics.serway_8_4(),
physics.serway_8_6(),
physics.serway_8_7(),
physics.serway_8_8(),
physics.serway_8_11()
)


#populate a set of all the items
total_items_list = []
for i in range(len(questionList)):
    total_items_list.append(i)
    
    
#choose a smaller subset from these questions
items_list = random.sample(total_items_list, round(1 * len(questionList)))


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
