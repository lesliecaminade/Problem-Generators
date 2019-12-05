import randomizer
import random_handler as ran
#import sympy_handler as symh
#import numpy_handler as num
import sympy as sym
from sympy import init_printing
from sympy import oo

import math
import math_common
import random
import stringHandling


import wave_propagation as wp

x, y = sym.symbols('x y', real = True)

import constants_conversions as c
from constants_conversions import *
from common_names import *




#test code
#from IPython.display import display
init_printing(use_unicode = False)
#display(yourobject) --- > to display new objects

solutions_flag = False

title_string = """Wave Propagation
Coded by Leslie Caminade June 2019
www.lesliecaminadecom.wordpress.com"""

questionList = (
wp.jma_5_43(),
wp.jma_5_44_a(),
wp.jma_5_44_b(),
wp.jma_5_45_a(),
wp.jma_5_45_b(),
wp.jma_5_46(),
wp.jma_5_51(),
wp.jma_5_52(),
wp.jma_5_55()
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
    if command == 'exit':
        stay = False
