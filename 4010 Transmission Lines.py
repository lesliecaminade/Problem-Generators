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


import transmission_lines as tl

x, y = sym.symbols('x y', real = True)

import constants_conversions as c
from constants_conversions import *
from common_names import *




#test code
#from IPython.display import display
init_printing(use_unicode = False)
#display(yourobject) --- > to display new objects

solutions_flag = False

title_string = """Transmission Lines
Coded by Leslie Caminade July 2019
www.lesliecaminadecom.wordpress.com"""

questionList = (
tl.jma_3_6(),
tl.jma_3_8(),
tl.jma_3_9_a(),
tl.jma_3_9_b(),
tl.jma_3_10(),
tl.jma_3_11(),
tl.jma_3_12(),
tl.jma_3_13(),
tl.jma_3_14_a(),
tl.jma_3_14_b(),
tl.jma_3_18(),
tl.jma_3_20(),
tl.jma_3_21(),
tl.jma_3_22(),
tl.jma_3_23(),
tl.jma_3_29_a(),
tl.jma_3_29_b(),
tl.jma_3_29_c(),
tl.jma_3_31(),
tl.jma_3_32_a(),
tl.jma_3_32_b()
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
