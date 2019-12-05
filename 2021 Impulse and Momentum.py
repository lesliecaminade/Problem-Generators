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
import physics as p
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

title_string = """Impulse and Momentum
Schaums, ...
Coded by Leslie Caminade June 2019
June 26 2019 - Changed the way questions are selected.
www.lesliecaminadecom.wordpress.com
note: 
 - log(x) refers to the natural logarithm
 - constant of integration is not added by itself"""

questionList = (
p.schaums_8_1(),
p.schaums_8_2(),
p.schaums_8_3(),
p.schaums_8_4(),
p.schaums_8_5(),
p.schaums_8_6(),
#p.schaums_8_7(),
p.schaums_8_9(),
p.schaums_8_10(),
p.schaums_8_11(),
#p.schaums_8_12(),
p.schaums_8_13(),
p.schaums_8_14(),
p.schaums_8_15(),
p.schaums_8_16(),
p.schaums_8_17()
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
