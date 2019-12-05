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


import physics as physics

x, y = sym.symbols('x y', real = True)

import constants_conversions as c
from constants_conversions import *
from common_names import *




#test code
#from IPython.display import display
init_printing(use_unicode = False)
#display(yourobject) --- > to display new objects

solutions_flag = False

title_string = """Hyrostatics
Coded by Leslie Caminade July 2019
www.lesliecaminadecom.wordpress.com"""

questionList = (
physics.schaums_13_1(),
physics.schaums_13_2(),
physics.schaums_13_3(),
physics.schaums_13_4(),
physics.schaums_13_5(),
physics.schaums_13_6(),
physics.schaums_13_7(),
physics.schaums_13_8(),
physics.schaums_13_9(),
physics.schaums_13_10(),
physics.schaums_13_11(),
physics.schaums_13_12(),
physics.schaums_13_13(),
physics.schaums_13_14(),
physics.schaums_13_15(),
physics.schaums_13_16(),
physics.schaums_13_17(),
physics.schaums_13_18(),
physics.schaums_13_19(),
physics.schaums_13_20(),
physics.schaums_13_21(),
physics.schaums_13_22(),
#physics.schaums_13_23(),
physics.schaums_13_24()
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
